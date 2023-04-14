from core.element import Element
from utils.ui_utils import LocatorType


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get("https://petstore.octoperf.com/actions/Account.action?signonForm=")

    def username_input(self):
        return Element(self.driver, LocatorType.NAME, "username")

    def password_input(self):
        return Element(self.driver, LocatorType.NAME, "password")

    def log_in_button(self):
        return Element(self.driver, LocatorType.NAME, "signon")

    def error_message(self):
        return Element(self.driver, LocatorType.XPATH, "//ul[contains(@class, 'messages')]/li")  # TODO: /text() too or you get that in the action as get text?
