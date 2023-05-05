from config import UI_BASE_URI
from core.element import Element
from utils.ui_utils import LocatorType


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Cart.action?viewCart=")

    def quantity_input(self, description):
        return Element(self.driver, LocatorType.XPATH, f"//td[normalize-space(text()) = '{description}']/..//input")

    def pet_description_info(self, description):
        return Element(self.driver, LocatorType.XPATH, f"//td[normalize-space(text()) = '{description}']")

    def checkout_button(self):
        return Element(self.driver, LocatorType.XPATH, "//a[normalize-space(text()) = 'Proceed to Checkout']")

    def not_logged_in_error_message(self):
        return Element(self.driver, LocatorType.XPATH, "//ul['messages']/li")

    def empty_cart_message(self):
        return Element(self.driver, LocatorType.XPATH, "//b[contains(text(), 'Your cart is empty.')]")
