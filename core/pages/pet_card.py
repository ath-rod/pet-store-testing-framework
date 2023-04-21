from core.element import Element
from utils.ui_utils import LocatorType


class PetCardPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_button(self):
        return Element(self.driver, LocatorType.XPATH, "//a[contains(text(), 'Add to Cart')]")
