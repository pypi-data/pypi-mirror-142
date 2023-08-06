import io
import logging
import os
from datetime import datetime
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from . import settings


def auth_check(f):
    def deco(self, *args, **kwargs):
        if not self.is_authenticated:
            self.login()
        return f(self, *args, **kwargs)

    return deco


class BaseClient(requests.Session):
    debug_captcha = False

    def __init__(self, credentials, base_domain=None):
        super(BaseClient, self).__init__()
        self.credentials = credentials
        self.base_domain = base_domain or self.default_domain

    @property
    def default_domain(self):
        raise NotImplementedError

    def captcha_solver(self, img, **kwargs):
        """
        captcha solver
        """
        origin_img = img

        if isinstance(img, str):
            img = io.StringIO(img)

        if isinstance(img, bytes):
            img = io.BytesIO(img)

        r = self.post(settings.CAPTCHA_API, data=kwargs, files=dict(file=img))
        captcha = r.text.replace(' ', '')

        if self.debug_captcha:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            with open(BASE_DIR + '/test_captcha/{}.bmp'.format(captcha), 'wb') as f:
                f.write(origin_img)
                logging.info('Captcha: {}'.format(captcha))

        return r.text.replace(' ', '')

    @property
    def username(self):
        return self.credentials.get('username')

    @property
    def password(self):
        return self.credentials.get('password')

    @property
    def base_uri(self):
        return urlparse(self.base_domain)

    @property
    def root(self):
        raise NotImplementedError

    def _url(self, path):
        return '{origin.scheme}://{origin.netloc}/{path}'.format(
            path=path.lstrip('/'),
            origin=self.base_uri
        )

    @staticmethod
    def str2time(text):
        if isinstance(text, str):
            return datetime.fromisoformat(text)

        return text

    @staticmethod
    def format_float(text):
        return float(text.replace(',', ''))

    @staticmethod
    def format_date(date_time):
        raise NotImplementedError

    @staticmethod
    def get_form(html, **kwargs):
        soup = BeautifulSoup(html, 'html.parser')
        form = soup.find('form', attrs=kwargs)
        target_url = form.get('action')
        form_data = dict(map(lambda n: (n.get('name'), n.get('value')), form.find_all('input')))

        return target_url, form_data
