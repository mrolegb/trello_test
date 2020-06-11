import os, requests, json

BOARDS_URL = "https://api.trello.com/1/boards/"
CARDS_URL = "https://api.trello.com/1/cards/"
MEMBERS_URL = "https://api.trello.com/1/members"


def trello_call(call, url, params={}):
    if os.environ['KEY'] and os.environ ['TOKEN']:
        key = os.environ['KEY']
        token = os.environ['TOKEN']
    else:
        from tests.trello.secure import TRELLO_KEY, TRELLO_TOKEN
        key = TRELLO_KEY
        token = TRELLO_TOKEN

    secure = {
        'key': key,
        'token': token
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
    if os.environ['member_id']:
        member_id = os.environ['member_id']
    else:
        from tests.trello.secure import MEMBER_ID
        member_id = MEMBER_ID

    _, boards = trello_call("GET", MEMBERS_URL + '/' + member_id + '/boards')
    for board in json.loads(boards):
        trello_call("DELETE", BOARDS_URL + board['id'])
