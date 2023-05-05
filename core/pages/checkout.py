from config import UI_BASE_URI
from core.element import Element
from utils.ui_utils import LocatorType


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Order.action?newOrderForm=")

    def first_name_input(self):
        return Element(self.driver, LocatorType.NAME, "order.billToFirstName")

    def last_name_input(self):
        return Element(self.driver, LocatorType.NAME, "order.billToLastName")

    def main_address_input(self):
        return Element(self.driver, LocatorType.NAME, "order.billAddress1")

    def continue_button(self):
        return Element(self.driver, LocatorType.NAME, "newOrder")
