import requests

from tests.steps.trello.secure import TRELLO_KEY, TRELLO_TOKEN


def trello_call(call, url, params={}):
    secure = {
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN
    }
    query = {**params, **secure}
    res = requests.request(call, url, params=query)
    return res.status_code, res.text
