import functools
from collections import defaultdict

from api_helper import get_uri, captcha_solver

from .exceptions import CaptchaError, AuthenticationError
from .parsers import parse_reports, get_name_rank, get_login_error
from .settings import HK_AGENT_DOMAIN
from .utils import sum_reduce, format_date


def get_captcha(session, domain):
    r = session.get(get_uri('auth/captcha/', domain), params={'reload': 'true'})
    r = session.get(get_uri(r.text, domain))
    return captcha_solver(r.content)


def login_error_hook(r, *args, **kwargs):
    error = get_login_error(r.text)
    if error:
        if 'Mã CODE sai' in error:
            raise CaptchaError

        raise AuthenticationError(error)


def login(session, username, password, domain=None):
    if domain is None:
        domain = HK_AGENT_DOMAIN

    captcha = get_captcha(session, domain)
    login_data = {
        'username': username,
        'password': password,
        'validation': captcha
    }

    if 'sub' in username.lower():
        login_data.update({'is_viewer': 1})

    session.post(get_uri('auth/login', domain), data=login_data, hooks={'response': login_error_hook})
    return domain


def profile(session, domain):
    if not hasattr(session, 'acc_profile'):
        r = session.get(get_uri('', domain))
        result = get_name_rank(r.text)

        setattr(session, 'acc_profile', result)
    else:
        print('serve from cache')
    return getattr(session, 'acc_profile')


def get_report(session, domain, start, end):
    r = session.get(get_uri('invoices/agent', domain), params={
        'start': format_date(start),
        'end': format_date(end)
    })

    name, _ = profile(session, domain)

    children_reports = list(parse_reports(r.text))
    parent_sum = functools.reduce(sum_reduce, children_reports, defaultdict(int))
    parent_reports = [(name, k, v) for k, v in parent_sum.items()]

    reports = children_reports + parent_reports
    return [('lotto', *_) for _ in reports]
