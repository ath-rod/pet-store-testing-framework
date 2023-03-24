from core.element import Element
from utils.ui_utils import LocatorType


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")

    def sidebar_cat_option(self):
        return Element(self.driver, LocatorType.XPATH, "//div[@id='Sidebar']//a[href$='CATS']")  # TODO: fix xpath
