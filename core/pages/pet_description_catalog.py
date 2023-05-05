from core.element import Element
from utils.ui_utils import LocatorType


class PetDescriptionCatalogPage:
    def __init__(self, driver):
        self.driver = driver

    def pet_item_id(self, description):
        return Element(self.driver, LocatorType.XPATH, f"//td[normalize-space(text()) = '{description}']"
                                                       f"/preceding-sibling::td/a")

    def pet_add_to_cart_button(self, description):
        return Element(self.driver, LocatorType.XPATH, f"//td[normalize-space(text()) = '{description}']"
                                                       f"/following-sibling::td/a")
