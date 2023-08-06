import os
from collections import defaultdict
from functools import cached_property
from urllib.parse import urlparse
from datetime import datetime, timedelta

import logging
import requests
from bs4 import BeautifulSoup
from api_helper.captcha import captcha_solver

from . import settings, exceptions


def get_form(html, **kwargs):
    soup = BeautifulSoup(html, 'html.parser')
    form = soup.find('form', attrs=kwargs)
    target_url = form.get('action')
    form_data = dict(map(lambda n: (n.get('name'), n.get('value')), form.find_all('input')))

    return target_url, form_data


def get_login_error(html):
    soup = BeautifulSoup(html, 'html.parser')
    error = soup.find(attrs={'id': 'wErrMsg'})
    if error:
        return error.text


def auth_check(f):
    def deco(self, *args, **kwargs):
        if not self.is_authenticated:
            self.login()
        return f(self, *args, **kwargs)

    return deco


class Sgd777Client(requests.Session):
    is_authenticated = False
    debug_captcha = False

    def __init__(self, credentials, base_domain=None):
        super(Sgd777Client, self).__init__()
        self.credentials = credentials
        self.base_domain = base_domain or settings.SGD777_AGENT_DOMAIN

    @property
    def username(self):
        return self.credentials.get('username')

    @property
    def password(self):
        return self.credentials.get('password')

    @property
    def base_uri(self):
        return urlparse(self.base_domain)

    def _url(self, path):
        return '{origin.scheme}://{origin.netloc}/{path}'.format(
            path=path.lstrip('/'),
            origin=self.base_uri
        )

    @property
    def login_url(self):
        return self._url('Login.aspx')

    @property
    def captcha_url(self):
        return self._url('VerifyCode.aspx')

    @property
    def profile_url(self):
        return self._url('header.aspx')

    @property
    def win_lose_url(self):
        return self._url('Reports/WinLose.aspx')

    @property
    def captcha(self):
        while True:
            r = self.get(self.captcha_url)
            captcha = captcha_solver(r.content, filters='clean_noise', whitelist='0123456789')

            if self.debug_captcha:
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
                with open(BASE_DIR + '/test_captcha/{}.bmp'.format(captcha), 'wb') as f:
                    f.write(r.content)
                    logging.info('Captcha: {}'.format(captcha))

            if len(captcha) == 4:
                return captcha
            else:
                logging.error('Wrong captcha {}'.format(captcha))

    @staticmethod
    def login_error_hook(r, **kwargs):
        if r.status_code != 200:
            return

        error = get_login_error(r.text)

        if error:
            if 'Verification Code error' in error:
                raise exceptions.CaptchaError(error)

            raise exceptions.AuthenticationError(error)

    MAX_LOGIN_TRY = 10

    def login(self):
        tried = 0
        while tried < self.MAX_LOGIN_TRY:
            tried += 1
            try:
                r = self.get(self.login_url)
                _, form_data = get_form(r.text, id='form1')

                form_data.update({
                    'wUserId': self.username,
                    'wPassword': self.password,
                    'txtVerCode': self.captcha,
                    # 'txtVerCode': '7155',
                    'wLang': 2,
                    'submitButton.x': 173,
                    'submitButton.y': 25
                })

                self.post(self.login_url, data=form_data, hooks={'response': self.login_error_hook})
                self.is_authenticated = True
                return
            except exceptions.CaptchaError:
                pass

    _profile = None

    @staticmethod
    def get_name(html):
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find(id='lblConCreteID')

        if info:
            return info.text

    @cached_property
    @auth_check
    def profile(self):
        r = self.get(self.profile_url)
        return self.get_name(r.text), ''

    @property
    def root(self):
        return self.profile[0]

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
        return date_time.strftime('%Y-%m-%d')

    def parse_row(self, row):
        cols = row.find_all('td')
        return {
            'username': cols[1].text.lower(),
            'turnover': self.format_float(cols[3].text),
            'net_turnover': self.format_float(cols[5].text),
            'win_lose': self.format_float(cols[4].text),
            'commission': self.format_float(cols[8].text),
        }

    def parse_report(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(id='detailsGrid')
        if table:
            rows = table.find_all('tr')[1:-1]
            return list(map(self.parse_row, rows))

        return []

    @auth_check
    def win_lose(self, from_date, to_date):
        _start = self.str2time(from_date)
        _end = self.str2time(to_date) + timedelta(days=1)

        r = self.get(self.win_lose_url)
        _, form_data = get_form(r.text, id='form1')

        data = form_data.copy()
        data.update({
            'wFromDate': self.format_date(_start),
            'wToDate': self.format_date(_end),
            'wTable': 999,
            'btnQuery': 'Query',
            # '__EVENTTARGET': 'AcctLinks1$LNK%s' % root,
            # '__EVENTARGUMENT': ''
        })

        r = self.post(self.win_lose_url, data=data)

        _, form_data2 = get_form(r.text, id='form1')

        form_data2.update({
            'wFromDate': self.format_date(_start),
            'wToDate': self.format_date(_end),
            'wTable': 999,
            'btnQuery': 'Query',
            '__EVENTTARGET': 'AcctLinks1$LNK%s' % self.root,
            '__EVENTARGUMENT': ''
        })

        form_data2.pop('btnQuery', None)

        r = self.post(self.win_lose_url, data=form_data2)

        reports = self.parse_report(r.text)

        root_report = defaultdict(int)

        for report in reports:
            yield report
            for k, v in report.items():
                if isinstance(v, (float, int)):
                    root_report[k] += v

        if len(root_report.keys()) > 0:
            yield dict(root_report, username=self.root.lower())
