import backoff
from requests.exceptions import RequestException

def _hdlr(details):
    print("网络错误，重试 {tries} 次，用时 {wait:0.1f} s".format(**details))

backoff_retry = backoff.on_exception(backoff.expo, RequestException, max_tries=10, on_backoff=_hdlr)
