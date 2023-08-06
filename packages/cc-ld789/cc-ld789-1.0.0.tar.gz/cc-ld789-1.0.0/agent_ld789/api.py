from collections import defaultdict

from .exceptions import AuthenticationError
from .settings import LD789_AGENT_DOMAIN
from .utils import get_be_url


def format_date(start):
    return start.strftime('%Y-%m-%d')


def auth_check(r, *args, **kwargs):
    json = r.json()
    if json is dict and json.get('message') == 'Unauthorized':
        print(r.request.headers)
        raise AuthenticationError('Unauthorized')


def login(session, username, password, code='BSWVKMUAOBD6WDUM', domain=None):
    if domain is None:
        domain = LD789_AGENT_DOMAIN

    data = {
        # 'grant_type': 'password',
        'Scope': 'backend',
        'Username': username,
        'Password': password,
        # 'otp': ''
    }
    # otp = {
    #     'otp': pyotp.TOTP(code).now()
    # }
    # data.update(otp)

    # r = session.post(get_be_url('auth/sign-in', domain), params=otp, data=data)
    r = session.post(get_be_url('auth/sign-in', domain), json=data)

    error = r.json().get('message')

    if error:
        raise AuthenticationError(error)

    session.headers.update({
        'authorization': 'Bearer %s' % r.json().get('IdToken'),
        'referer': 'https://ag.one789.net/'
    })

    session.hooks['response'] = [auth_check]

    # TODO recheck
    # me = get_user(session, domain, 'me')
    #
    # if me.get('mustChangePassword'):
    #     change_password(session, domain, password, password+'@@@')
    #     change_password(session, domain, password+'@@@', password)
    #
    # if me.get('mustEnableTfa'):
    #     register_otp(session, domain)
    return domain


def change_password(session, domain, old_password, new_password):
    return session.put(get_be_url('api/user/me/password', domain), {
        'OldPassword': old_password,
        'NewPassword': new_password
    })


def get_user(session, domain, user='me'):
    return session.get(get_be_url('api/user/%s' % user, domain)).json()


def profile(session, domain):
    cache_key = 'acc_profile'
    if not hasattr(session, cache_key):
        r = session.get(get_be_url('users/profile', domain)).json()
        data = r.get('Username').lower().split('sub')[0], ''

        setattr(session, cache_key, data)

    return getattr(session, cache_key)


def parse_report(i, root):
    username = i.get('Username').lower()
    yield username, 'turnover', i.get('Player').get('NetAmount') / 1000
    yield username, 'win_lose', i.get('Player').get('WinLose') / 1000


def get_report(session, domain, start, end, root=None):
    if root is None:
        root, _ = profile(session, domain)

    uri = get_be_url('statements/agent/statements/children-user', 'https://report.lotusapi.com/')
    r = session.get(uri, params={
        'from': format_date(start),
        'to': format_date(end),
        'productTypes': [0, 1, 2, 100],
        'size': 100,
        'page': 1
    })

    base_data = defaultdict(int)

    for i in r.json():
        for item in parse_report(i, root):
            yield 'lotto', *item

            if isinstance(item[2], (float, int)):
                base_data[item[1]] += item[2]

    for k, v in base_data.items():
        yield 'lotto', root, k, v


def get_otp_info(session, domain):
    r = session.get(get_be_url('api/user/me/tfa', domain))
    return r.text


def register_otp(session, domain, seed='BSWVKMUAOBD6WDUM'):
    r = session.put(get_be_url('api/user/me/tfa', domain), data={
        'Enable': True,
        'Psk': seed,
        # 'Otp': pyotp.TOTP(seed).now()
    })

    return r.text


def unregister_otp(session, domain, seed='BSWVKMUAOBD6WDUM'):
    r = session.put(get_be_url('api/user/me/tfa', domain), data={
        'Enable': False,
        'Psk': seed,
    })

    return r.text


def get_psk(session, domain):
    return session.get(get_be_url('api/user/tfa/generatepsk', domain)).json().get('psk')
