from tests.trello.pages.board import BoardPage
from tests.trello.pages.card import CardPage
from tests.trello.pages.main import MainPage
from tests.trello.pages.login import LoginPage
from time import sleep


def test_find_commented_card(browser):
    login_page = LoginPage(browser)
    login_page.navigate_to()
    login_page.login()

    main_page = MainPage(browser)
    assert main_page.is_loaded()

    board = main_page.find_board_with_name('Test board')
    board.click()

    board_page = BoardPage(browser)
    assert board_page.is_loaded()

    sleep(1)

    card = board_page.find_card_by_order(0)
    card.click()

    card_page = CardPage(browser)
    assert card_page.is_loaded()

    assert card_page.find_comment('Hello world')


def test_find_updated_card(browser):
    login_page = LoginPage(browser)
    login_page.navigate_to()
    login_page.login()

    main_page = MainPage(browser)
    assert main_page.is_loaded()

    board = main_page.find_board_with_name('Test board')
    board.click()

    board_page = BoardPage(browser)
    assert board_page.is_loaded()

    sleep(1)

    card = board_page.find_card_by_order(1)
    card.click()

    sleep(1)

    card_page = CardPage(browser)
    assert card_page.is_loaded()

    assert card_page.get_card_title() == 'New name'
