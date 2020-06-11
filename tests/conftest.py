import pytest

from tests.trello.api import create_board, delete_boards
from selenium import webdriver


@pytest.fixture(scope='session')
def board(request):
    board_id = create_board()
    yield board_id
    delete_boards()


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
