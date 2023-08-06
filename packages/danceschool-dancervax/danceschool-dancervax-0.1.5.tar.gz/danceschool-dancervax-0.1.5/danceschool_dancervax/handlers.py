from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

import logging
import requests
from datetime import date
import base64
import json

from danceschool.core.constants import getConstant
from danceschool.core.models import EventRegistration
from danceschool.core.signals import get_eventregistration_data, get_person_data

from .session import dancervax_session


# Define logger for this file
logger = logging.getLogger(__name__)


def encode_key(value):
    '''
    Use JSON and base64 to create cache keys that are compatible with
    cache backends that accept only strings.
    '''
    return 'danceschool_dancervax_{}'.format(
        base64.b64encode(bytes(json.dumps(value), 'utf-8'))
    )


@receiver(get_eventregistration_data)
def checkDancerVax(sender, **kwargs):
    '''
    Look up DancerVax status using the API.
    '''
    eventregistrations = kwargs.get('eventregistrations', EventRegistration.objects.none())
    event_date = kwargs.get('event_date', date.today())
    names = kwargs.get('names', [])

    if (
        not (eventregistrations or names) or not
        getConstant('registration__enableDancerVaxLookup')
    ):
        return

    if not dancervax_session.session:
        logger.debug('DancerVax API session not set up.')
        return

    reg_details = []
    cached_response = {}

    for x in eventregistrations.filter(customer__isnull=False):
        this_info = (x.id, x.customer.first_name, x.customer.last_name, x.customer.email)

        cached_value = cache.get(encode_key(this_info))
        if cached_value:
            cached_response[x.id] = cached_value
        else:
            reg_details.append(this_info)

    for x in names:
        this_info = (x['email'], x['first_name'], x['last_name'], x['email'])

        cached_value = cache.get(encode_key(this_info))
        if cached_value:
            cached_response[x['email']] = cached_value
        else:
            reg_details.append(this_info)

    lookup_data = {
        'event_date': event_date.strftime('%Y-%m-%d'),
        'details': [(x[1], x[2], x[3]) for x in reg_details],
    }

    if not lookup_data['details'] and not cached_response:
        logger.debug('No customer information to lookup.')
        return

    logger.debug("Preparing to check DancerVax")
    lookup_response = dancervax_session.submit(lookup_data)

    extras = cached_response

    for er in reg_details:

        found = next(
            (
                item for item in lookup_response if
                item.get('user', {}).get("first_name") == er[1] and
                item.get('user', {}).get("last_name") == er[2] and 
                item.get('user', {}).get("email") == er[3] 
            ),
            None
        )

        if found:
            this_response = [{
                'id': er[0],
                'name': _('Vaccination Status Lookup'),
                'type': 'vaccine_lookup',
                'amount': 0,
                'response': found,
            },]
            if found.get('vaxStatus') == 'Approved':
                cache.set(encode_key(er), this_response, timeout=86400)
            else:
                cache.set(encode_key(er), this_response, timeout=300)
            extras[er[0]] = this_response
    return extras


@receiver(get_person_data)
def checkDancerVaxPerson(sender, **kwargs):
    is_single = False
    names = []

    if kwargs.get('first_name') and kwargs.get('last_name') and kwargs.get('email'):
        names = [{
            'first_name': kwargs.get('first_name'),
            'last_name': kwargs.get('last_name'),
            'email': kwargs.get('email'),
        }]
        is_single = True
    else:
        for name in kwargs.get('names', []):
            names.append({
                'first_name': name.get('first_name', name.get('firstName', name.get('first', ''))),
                'last_name': name.get('last_name', name.get('lastName', name.get('last', ''))),
                'email': name.get('email', name.get('contact', '')),
            })

    names = [x for x in names if x['first_name'] and x['last_name'] and x['email']]

    if names:
        response = checkDancerVax(sender, names=names)
        if is_single and response.get(kwargs.get('email')):
            return response.get(kwargs.get('email'))[0]
        else:
            return response
