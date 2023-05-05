from config import UI_BASE_URI
from core.element import Element
from utils.ui_utils import LocatorType


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Account.action?signonForm=")

    def username_input(self):
        return Element(self.driver, LocatorType.NAME, "username")

    def password_input(self):
        return Element(self.driver, LocatorType.NAME, "password")

    def log_in_button(self):
        return Element(self.driver, LocatorType.NAME, "signon")

    def error_message(self):
        return Element(self.driver, LocatorType.XPATH, "//ul['messages']/li")
