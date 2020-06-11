from tests.trello.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class BoardPage(BasePage):

    def is_loaded(self):
        return self.find_element((By.CLASS_NAME, 'board-main-content'))

    def find_card_by_order(self, order):
        sleep(1)
        cards = self.find_elements((By.CSS_SELECTOR, 'a[class^="list-card"]'))
        return cards[order]
