from config import UI_BASE_URI
from core.element import Element
from utils.ui_utils import LocatorType


class ConfirmCheckoutInformationPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Order.action")

    def confirm_button(self):
        return Element(self.driver, LocatorType.XPATH, "//a[contains(text(), 'Confirm')]")
    