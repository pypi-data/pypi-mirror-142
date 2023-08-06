from datetime import datetime

import requests
from celery import shared_task, Celery
from celery.utils.log import get_task_logger

from . import api

LOG = get_task_logger(__name__)

# new tasks


app = Celery('hk')


def login(auth):
    session = requests.session()
    domain = api.login(session, auth.get('username'), auth.get('password'))
    return session, domain


@shared_task(bind=True, name='hk.profile')
def profile(self, auth):
    session, domain = login(auth)
    return api.profile(session, domain)


@shared_task(name='hk.tickets')
def get_tickets(auth, from_date, to_date=None):
    pass


def sum_reduce(a, b):
    a[b[1]] += b[2]
    return a


@shared_task(name='hk.win_lose', max_retries=2)
def get_win_lose(auth, from_date, to_date, *args):
    from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
    to_date = datetime.fromisoformat(to_date) if isinstance(to_date, str) else to_date

    session, domain = login(auth)
    name, _ = api.profile(session, domain)

    return {
        'username': name,
        'from_date': from_date.date().isoformat(),
        'to_date': to_date.date().isoformat(),
        'data': api.get_report(session, domain, from_date, to_date)
    }
