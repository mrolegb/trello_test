import pytest

from tests.trello.api import create_board
from selenium import webdriver


@pytest.fixture(scope='session')
def board(request):
    board_id = create_board()
    return board_id


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
