from collections import defaultdict

from bs4 import BeautifulSoup

from .utils import get_uri
from . import settings


def format_date(start):
    return start.strftime('%Y-%m-%d')


def format_float(text):
    return float(text.replace(',', ''))


def patch_session(session):
    session.headers.update(settings.DEFAULT_HEADERS)


def login(session, username, password, domain=None):
    # init request to create session
    # session.get(get_uri('login', domain))

    session.headers.update(settings.DEFAULT_HEADERS)

    if domain is None:
        domain = settings.LVS_AGENT_DOMAIN

    data = {
        'account': username,
        'passwd': password
    }

    # actual login request
    r = session.post('https://edy688.com/auth', params=data)

    return domain


def get_name_rank(html):
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find(attrs={'id': 'login-info'}).find_all('span')
    return [i.text.lower().split('sub')[0] for i in info]


def profile(session, domain):
    r = session.get(get_uri('', domain))
    return get_name_rank(r.text)


def parse_report(row):
    cols = row.find_all('td')

    username = cols[1].text.lower()

    yield username, 'turnover', format_float(cols[5].text)
    yield username, 'net_turnover', format_float(cols[12].text)
    yield username, 'commission', format_float(cols[7].text)
    yield username, 'win_lose', format_float(cols[9].text)


def parse_reports(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find('tbody').find_all('tr', attrs={'class': 'report-info'})

        for i in rows:
            yield from parse_report(i)

    except AttributeError:
        pass


def get_report(session, domain, start, end, root=None):
    if root is None:
        root, _ = profile(session, domain)

    r = session.get(get_uri('report/info', domain), params={
        'start': format_date(start),
        'end': format_date(end),
        'timetype': 0,
        'servo': ''
    }, headers={'x-requested-with': 'XMLHttpRequest'})

    base_data = defaultdict(int)

    for item in parse_reports(r.text):
        yield 'casino', *item
        if isinstance(item[2], (float, int)):
            base_data[item[1]] += item[2]

    for k, v in base_data.items():
        yield 'casino', root, k, v
