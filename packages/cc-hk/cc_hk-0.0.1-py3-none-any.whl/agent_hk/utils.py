import io
from urllib.parse import urlparse

import requests

from . import settings


def captcha_solver(img, **kwargs):
    if isinstance(img, str):
        img = io.StringIO(img)

    if isinstance(img, bytes):
        img = io.BytesIO(img)

    r = requests.post(settings.CAPTCHA_API, data=kwargs, files=dict(file=img))

    return r.text


def get_uri(uri='', base=None):
    return (base or settings.HK_AGENT_DOMAIN) + uri


def get_base_url(origin):
    url = urlparse(origin)  # type: ParseResult
    return url.scheme + "://" + url.netloc + '/'


def sum_reduce(a, b):
    a[b[1]] += b[2]
    return a


def format_date(date_time):
    return date_time.strftime('%d-%m-%Y')


def format_float(text):
    return float(text.replace(',', ''))


def get_upline(text):
    return '.'.join(text.split('.')[:-1])
