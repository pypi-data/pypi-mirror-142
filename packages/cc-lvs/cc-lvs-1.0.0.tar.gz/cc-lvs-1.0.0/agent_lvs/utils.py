import io
import random
import string
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


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def encrypt_string(encryption_exponent, encryption_modulus, string_to_encrypt):
    return requests.get('https://ok368.lehongnam.com',
                        params=dict(expo=encryption_exponent, modulus=encryption_modulus, str=string_to_encrypt)
                        ).text


def get_uri(uri='', base=None):
    return (base or settings.LVS_AGENT_DOMAIN) + uri


def get_be_url(uri, base):
    return get_uri(uri, base.replace('ag.', 'be.'))


def get_base_url(origin):
    url = urlparse(origin)  # type: ParseResult
    return url.scheme + "://" + url.netloc + '/'
