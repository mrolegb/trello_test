import requests, json

from pytest_bdd import scenario, given, when, then, parsers

from tests.steps.trello.api import trello_call
from tests.steps.trello.secure import TRELLO_KEY, TRELLO_TOKEN


BOARDS_URL = "https://api.trello.com/1/boards/"

context = {}


@scenario('../feature/trello.feature', 'Create a board and retrieve it')
def test_api():
    pass


@given(parsers.parse('a new board named {name} was created'))
def new_board(name):
    params = {
        'name': name
    }

    code, results = trello_call("POST", BOARDS_URL, params)

    assert code == 200
    context['board_id'] = json.loads(results)['id']


@when('I fetch the board by id')
def get_board():
    code, results = trello_call("GET", BOARDS_URL + context['board_id'])

    assert code == 200
    context['last_response'] = json.loads(results)


@then(parsers.parse('I can verify the board name is {name}'))
def verify_name(name):
    assert context['last_response']['name'] == name
