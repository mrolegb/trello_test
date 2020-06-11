import pytest

from tests.trello.api import create_board


@pytest.fixture(scope='session')
def board(request):
    board_id = create_board()
    return board_id
