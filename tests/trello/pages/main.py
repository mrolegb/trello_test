from tests.trello.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(BasePage):

    def is_loaded(self):
        return self.find_element((By.XPATH, '//*[@id="header"]/div[1]/button'))

    def find_board_with_name(self, name):
        sleep(1)
        boards = self.find_elements((By.CLASS_NAME, 'board-tile'))
        for b in boards:
            title = b.find_element(By.CLASS_NAME, 'board-tile-details-name')
            if title.get_attribute('title') == name:
                return b
