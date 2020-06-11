import json

from tests.trello.api import trello_call, get_list_by_name, create_card, CARDS_URL, MEMBERS_URL, BOARDS_URL


def test_create_card_and_comment(board):
    board_id = board
    to_do_list = get_list_by_name(board_id, 'To Do')

    code, results = create_card(to_do_list)
    assert code == 200

    card_id = json.loads(results)['id']

    params = {
        'text': 'Hello world'
    }

    code, _ = trello_call("POST", CARDS_URL + card_id + '/actions/comments', params=params)
    assert code == 200

    code, results = trello_call("GET", CARDS_URL + card_id)
    assert code == 200

    comments = json.loads(results)['badges']['comments']
    assert comments == 1


def test_create_update_card(board):
    board_id = board
    to_do_list = get_list_by_name(board_id, 'To Do')

    code, results = create_card(to_do_list)
    assert code == 200

    card_id = json.loads(results)['id']

    params = {
        'name': 'New name'
    }

    code, _ = trello_call("PUT", CARDS_URL + card_id, params=params)
    assert code == 200

    code, results = trello_call("GET", CARDS_URL + card_id)
    assert code == 200

    card_details = json.loads(results)
    assert card_details['name'] == 'New name'


def test_create_delete_card(board):
    board_id = board
    to_do_list = get_list_by_name(board_id, 'To Do')

    code, results = create_card(to_do_list)
    assert code == 200

    card_id = json.loads(results)['id']

    code, _ = trello_call("DELETE", CARDS_URL + card_id)
    assert code == 200

    code, result = trello_call("GET", CARDS_URL + card_id)
    assert code == 404


def _delete_boards():
    _, boards = trello_call("GET", MEMBERS_URL + '/user32772205' + '/boards')
    for board in json.loads(boards):
        trello_call("DELETE", BOARDS_URL + board['id'])

