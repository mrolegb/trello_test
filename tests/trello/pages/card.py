from tests.trello.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CardPage(BasePage):

    def is_loaded(self):
        return self.find_element((By.CSS_SELECTOR, 'div[class^="card-detail-window"]'))

    def get_card_title(self):
        self.find_element((By.CSS_SELECTOR, 'textarea[class^="mod-card-back-title"]')).click()
        return self.find_element((By.CSS_SELECTOR, 'textarea[class^="mod-card-back-title"]')).get_attribute('value')

    def find_comment(self, comment):
        comments = self.find_elements((By.CLASS_NAME, 'comment-container'))
        for c in comments:
            value = c.find_element(By.TAG_NAME, 'p').text
            if value == comment:
                return c

    def add_comment(self, comment):
        comment_input = self.find_element((By.CSS_SELECTOR, 'textarea[class*="js-new-comment-input"]'))
        comment_input.click()
        comment_input.clear()
        comment_input.send_keys(comment)

        self.find_element((By.CSS_SELECTOR, 'input[class*="js-add-comment"]')).click()
