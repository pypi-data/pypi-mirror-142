from bs4 import BeautifulSoup

from agent_hk.utils import format_float


def parse_row(row):
    cols = row.find_all('td')
    username = cols[1].find('a').text.lower()

    yield username, 'order_count', format_float(cols[2].text)
    yield username, 'origin:2d', format_float(cols[3].text)
    yield username, 'origin:3-4d', format_float(cols[4].text)

    yield username, '2d', format_float(cols[5].text)
    yield username, '3-4d', format_float(cols[6].text)
    yield username, 'win', format_float(cols[7].text)
    yield username, 'win_lose', format_float(cols[8].text)
    yield username, 'win_lose_percentage', format_float(cols[9].find('div').text)

    yield username, 'parent:2d', format_float(cols[10].text)
    yield username, 'parent:3-4d', format_float(cols[11].text)
    yield username, 'parent:win', format_float(cols[12].text)
    yield username, 'parent:win_lose', format_float(cols[13].text)
    yield username, 'parent:win_lose_percentage', format_float(cols[14].find('div').text)

    # extra info
    yield username, 'commission', format_float(cols[13].text) - format_float(cols[8].text)


def parse_reports(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find('tbody').find_all('tr')

    for row in rows:
        yield from parse_row(row)


def get_name_rank(html):
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find(attrs={'class': 'navbar-brand'}).find('b')
    rank, name = info.text.split(':')
    return name.lower().split('-')[0].split('sub')[0].strip(), rank.replace('panel', '').strip()


def get_login_error(html):
    soup = BeautifulSoup(html, 'html.parser')
    error = soup.find(attrs={'id': 'flashMessage'})
    if error:
        return error.text
