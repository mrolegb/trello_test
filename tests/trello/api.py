import requests, json

from tests.trello.secure import TRELLO_KEY, TRELLO_TOKEN, MEMBER_ID

BOARDS_URL = "https://api.trello.com/1/boards/"
CARDS_URL = "https://api.trello.com/1/cards/"
MEMBERS_URL = "https://api.trello.com/1/members"


def trello_call(call, url, params={}):
    secure = {
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN
    }
    query = {**params, **secure}
    res = requests.request(call, url, params=query)
    return res.status_code, res.text


def create_board():
    params = {
        'name': 'Test board'
    }

    _, results = trello_call("POST", BOARDS_URL, params)
    return json.loads(results)['id']


def get_list_by_name(board_id, name):
    _, response = trello_call("GET", BOARDS_URL + board_id + '/lists')
    lists = json.loads(response)
    my_list = None
    for ls in lists:
        if ls['name'] == name:
            my_list = ls
    return my_list['id']


def create_card(list_id):
    params = {
        'idList': list_id
    }
    return trello_call("POST", CARDS_URL, params=params)


def delete_boards():
    _, boards = trello_call("GET", MEMBERS_URL + '/' + MEMBER_ID + '/boards')
    for board in json.loads(boards):
        trello_call("DELETE", BOARDS_URL + board['id'])
