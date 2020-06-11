from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://trello.com/login"

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"No element found by locator {locator}")

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"No elements found by locator {locator}")

    def navigate_to(self):
        return self.driver.get(self.base_url)
