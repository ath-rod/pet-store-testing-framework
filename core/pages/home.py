from core.element import Element
from utils.ui_utils import LocatorType


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")

    def sidebar_pet_option(self, pet):
        return Element(self.driver, LocatorType.XPATH, f"//div[@id='Sidebar']//a[contains(@href,'{pet}')]")

    def welcome_user_message(self):
        return Element(self.driver, LocatorType.ID, "WelcomeContent")
