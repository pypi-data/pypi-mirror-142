import logging
from datetime import datetime

import requests
from celery import shared_task

from . import api
from api_helper import import_win_lose

LOG = logging.getLogger(__name__)

# new tasks


def login(auth):
    session = requests.session()
    domain = api.login(session, auth.get('username'), auth.get('password'))
    return session, domain


@shared_task(name='ld789.profile')
def profile(self, auth):
    session, domain = login(auth)
    return api.profile(session, domain)


@shared_task(name='ld789.tickets')
def get_tickets(auth, from_date, to_date=None):
    pass


@shared_task(name='ld789.win_lose')
def get_win_lose(auth, from_date, to_date, outstanding=False):
    from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
    to_date = datetime.fromisoformat(to_date) if isinstance(to_date, str) else to_date

    session, domain = login(auth)
    name, rank = api.profile(session, domain)

    return import_win_lose({
        'uuid': '-'.join([name, from_date.date().isoformat(), to_date.date().isoformat()]),
        'username': name,
        'from_date': from_date.date().isoformat(),
        'to_date': to_date.date().isoformat(),
        'data': api.get_report(session, domain, from_date, to_date)
    })
