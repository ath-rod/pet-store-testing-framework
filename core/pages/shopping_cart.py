from core.element import Element
from utils.ui_utils import LocatorType


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get("https://petstore.octoperf.com/actions/Cart.action?viewCart=")

    def quantity_input(self):
        return Element(self.driver, LocatorType.XPATH, "//tbody/tr[2]/td[5]/input")  # TODO: very ugly

    def checkout_button(self):
        return Element(self.driver, LocatorType.XPATH, "//a[contains(@href, 'newOrder')]")
