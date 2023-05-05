from core.element import Element
from utils.ui_utils import LocatorType
from config import UI_BASE_URI


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Catalog.action")

    def sidebar_pet_option(self, pet):
        return Element(self.driver, LocatorType.XPATH, f"//div[@id='Sidebar']//a[contains(@href,'{pet}')]")

    def top_bar_pet_option(self, pet):
        return Element(self.driver, LocatorType.XPATH, f"//div[@id='QuickLinks']/a[contains(@href,'{pet}')]")

    def welcome_user_message(self):
        return Element(self.driver, LocatorType.ID, "WelcomeContent")

    def distinctive_home_page_element(self):
        return Element(self.driver, LocatorType.ID, "Welcome")
