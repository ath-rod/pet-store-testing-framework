from core.element import Element
from utils.ui_utils import LocatorType
from config import UI_BASE_URI


class PetBreedCatalogPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, breed):
        self.driver.get(f"{UI_BASE_URI}/Catalog.action?viewCategory=&categoryId={breed}")

    def pet_breed(self, breed):
        return Element(self.driver, LocatorType.XPATH, f"//td[contains(text(),'{breed}')]/preceding-sibling::td/a")

    
class PetDescriptionCatalogPage:
    def __init__(self, driver):
        self.driver = driver

    def pet_item_id(self, description):
        return Element(self.driver, LocatorType.XPATH, f"//td[normalize-space(text()) = '{description}']"
                                                       f"/preceding-sibling::td/a")

    def pet_add_to_cart_button(self, description):
        return Element(self.driver, LocatorType.XPATH, f"//td[normalize-space(text()) = '{description}']"
                                                       f"/following-sibling::td/a")
