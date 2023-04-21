from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from utils.ui_utils import LocatorType


class Element:
    def __init__(self, driver, locator_type, locator):
        self.locator = locator
        self.web_element = driver.find_element(by=LocatorType.to_selenium_type(locator_type), value=self.locator)

    def click(self):
        self.web_element.click()
        print(f"Clicked {self.locator}")
        return self  # so you can page.web_element.click().other_action()

    def clear(self):
        self.web_element.clear()
        print(f"Cleared {self.locator}")
        return self

    def clear_and_send_keys(self, text):
        self.web_element.clear()
        self.web_element.send_keys(text)
        print(f"Cleared and sent '{text}' keys into {self.locator}")
        return self

    def select_option(self, option):
        Select(self.web_element).select_by_value(option)
        print(f"Selected {option} from {self.locator}")
        return self

    def get_text(self):
        text = self.web_element.text
        print(f"Obtained '{text}' text from {self.locator}")
        return text

    def get_text_from_input(self):
        text = self.web_element.get_attribute("value")
        print(f"Obtained '{text}' text from {self.locator} input")
        return text

    def press_enter(self):
        self.web_element.send_keys(Keys.ENTER)
        print(f"Pressed ENTER on {self.locator}")
        return self
