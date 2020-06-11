import os

from tests.trello.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def login(self):
        if os.environ['user'] and os.environ['password']:
            user = os.environ['user']
            password = os.environ['password']
        else:
            from tests.trello.secure import TRELLO_LOGIN, TRELLO_PASSWORD
            user = TRELLO_LOGIN
            password = TRELLO_PASSWORD

        user_field = self.find_element((By.CSS_SELECTOR, '#user'))
        user_field.click()
        user_field.send_keys(user)

        pass_field = self.find_element((By.CSS_SELECTOR, '#password'))
        pass_field.click()
        pass_field.send_keys(password)

        self.find_element((By.CSS_SELECTOR, '#login')).click()
