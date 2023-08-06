import re
import logging
from collections import defaultdict
from functools import reduce

from bs4 import BeautifulSoup

from .exceptions import AuthenticationError, CaptchaError
from .utils import get_uri, encrypt_string, random_word, captcha_solver
from .settings import OK368_AGENT_DOMAIN


def get_session_id(html):
    return re.findall(r'jsessionid=([a-zA-Z0-9\-\_]*)', html)[0]


def sign_url(url, domain, session_id):
    return '%s;jsessionid=%s' % (get_uri(url, domain), session_id)


def get_rsa_public_key(html):
    rsa_public_key_string = re.findall(r"var publicKey = new RSAKeyPair\('(.*?)'\);", html)[0]
    rsa_public_key_arr = rsa_public_key_string.split("', '', '")
    encryption_exponent = rsa_public_key_arr[0]
    encryption_modulus = rsa_public_key_arr[1]
    return encryption_exponent, encryption_modulus


def get_error_msg(html):
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find(attrs={'id': 'errMsg'})
    return info.text.strip() if info else None


def get_captcha(session, domain, session_id):
    while True:
        r = session.get(sign_url('validationCode/{}/'.format(random_word(8)), domain, session_id))
        captcha = captcha_solver(r.content, mode='ok368')

        if len(captcha) != 4:
            continue

        return captcha


def login(session, username, password, domain=None, **kwargs):
    if domain is None:
        domain = OK368_AGENT_DOMAIN

    r = session.get(get_uri('index.do', domain))
    session_id = get_session_id(r.text)

    r = session.get(get_uri('agent_login_standard.jsp', domain))
    encryption_exponent, encryption_modulus = get_rsa_public_key(r.text)

    enc_password = encrypt_string(encryption_exponent, encryption_modulus, password)
    captcha = get_captcha(session, domain, session_id)

    login_data = {
        'loginName': username,
        'password': enc_password,
        'mode': 'S',
        'randomCode': captcha
    }

    r = session.post(sign_url('agent/stdLogin.action', domain, session_id), data=login_data)

    # TODO detect login error

    if 'agent/main' not in r.url:
        error_message = get_error_msg(r.text)

        if 'Validate code error' in error_message:
            raise CaptchaError

        raise AuthenticationError(error_message)

    return domain, session_id


RANK_STR = {
    5: 'Super',
    6: 'Master',
    7: 'Agent'
}


def profile(session, domain, session_id):
    r = session.get(sign_url('agent/acct/list.action', domain, session_id))
    try:
        real_name = re.findall(r'var acctId = (.+);', r.text)[0].strip('\'"')
        rank = int(re.findall(r'var roleId = (.+);', r.text)[0].strip('\'"'))
        rank_str = RANK_STR.get(rank)

        return real_name, rank_str
    except:
        raise Exception(r.text)


def format_date(date_time):
    return date_time.strftime('%Y-%m-%d')


def reduce_report(a, b):
    return dict(
        turnover=a.get('turnover', 0) + b.get('turnover', 0),
        commission=a.get('commission', 0) + b.get('commission', 0),
        win_lose=a.get('win_lose', 0) + b.get('win_lose', 0),
    )


FIELDS = [
    'comm1', 'comm2', 'comm3', 'comm4', 'comm5', 'comm6', 'comm7', 'comm8',
    'comm1', 'comm2', 'comm3', 'comm4', 'comm5', 'comm6', 'comm7', 'comm8',
]


def parse_single_report(item):
    username = item.get('acctId').lower()
    for k, v in item.items():
        if isinstance(v, (int, float)) and v != 0:
            yield username, k, v

    yield username, 'turnover', item.get('share8')
    yield username, 'win_lose', item.get('wl8')


def parse_report(data, parent):
    if not data:
        return []

    base_data = defaultdict(int)

    for row in data:
        for item in parse_single_report(row):
            yield item

            base_data[item[1]] += item[2]

    for k, v in base_data.items():
        yield parent.lower(), k, v


def get_report(session, domain, session_id, from_date, to_date, ids=None):
    if ids is None:
        ids, _ = profile(session, domain, session_id)

    data = {
        'acctId': ids.upper(),
        'beginDate': format_date(from_date),
        'endDate': format_date(to_date),
        'finished': 'true',
    }

    r = session.post(sign_url('report/winLossDetail.action', domain, session_id), data=data)

    for _ in parse_report(r.json().get('list'), ids):
        yield 'lotto', *_
