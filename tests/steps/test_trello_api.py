import requests, json

from pytest_bdd import scenario, given, when, then, parsers

from trello.secure import TRELLO_KEY, TRELLO_TOKEN


BOARDS_URL = "https://api.trello.com/1/boards/"

context = {}


@scenario('../feature/trello.feature', 'Create a board and retrieve it')
def test_api():
    pass


@given(parsers.parse('a new board named {name} was created'))
def new_board(name):
    url = BOARDS_URL

    query = {
        'name': name,
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN
    }

    response = requests.request(
        "POST",
        url,
        params=query,
    )

    assert response.status_code == 200

    context['board_id'] = json.loads(response.text)['id']


@when('I fetch the board by id')
def get_board():
    url = BOARDS_URL

    query = {
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN
    }

    response = requests.request(
        "GET",
        url + context['board_id'],
        params=query
    )

    assert response.status_code == 200

    context['last_response'] = json.loads(response.text)


@then(parsers.parse('I can verify the board name is {name}'))
def verify_name(name):
    assert context['last_response']['name'] == name
