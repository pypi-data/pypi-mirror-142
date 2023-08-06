import backoff
import json
import requests
from datetime import datetime
from pathlib import Path
from requests.exceptions import RequestException

def _hdlr(details):
    print("网络错误，重试 {tries} 次，用时 {wait:0.1f} s".format(**details))

backoff_retry = backoff.on_exception(backoff.expo, RequestException, max_tries=10, on_backoff=_hdlr)


def get_cookies(session):
    cookies_path = Path.home().joinpath('badminton_cookies')
    if cookies_path.exists():
        with open(cookies_path, 'r', encoding='utf-8') as f:
            session.cookies = requests.utils.cookiejar_from_dict(json.load(f))
    else:
        with open(cookies_path, 'w', encoding='utf-8') as f:
            f.wirite(json.dumps(requests.utils.dict_from_cookiejar(session.cookies)))


def print_with_time(string):
    """print with time
    """
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {string}')
