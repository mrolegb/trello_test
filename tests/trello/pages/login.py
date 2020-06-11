from tests.trello.pages.base_page import BasePage
from selenium.webdriver.common.by import By

from tests.trello.secure import TRELLO_LOGIN, TRELLO_PASSWORD


class LoginPage(BasePage):

    def login(self):
        user_field = self.find_element((By.CSS_SELECTOR, '#user'))
        user_field.click()
        user_field.send_keys(TRELLO_LOGIN)

        pass_field = self.find_element((By.CSS_SELECTOR, '#password'))
        pass_field.click()
        pass_field.send_keys(TRELLO_PASSWORD)

        self.find_element((By.CSS_SELECTOR, '#login')).click()
