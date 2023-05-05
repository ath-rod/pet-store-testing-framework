from core.element import Element
from utils.ui_utils import LocatorType


class PetBreedCatalogPage:
    def __init__(self, driver):
        self.driver = driver

    def pet_breed(self, breed):
        return Element(self.driver, LocatorType.XPATH, f"//td[contains(text(),'{breed}')]/preceding-sibling::td/a")
