from enum import Enum, auto

from selenium.webdriver.common.by import By


class LocatorType(Enum):
    ID = auto()
    NAME = auto()
    XPATH = auto()
    CLASS_NAME = auto()

    @staticmethod
    def to_selenium_type(locator_type):
        match locator_type:
            case LocatorType.ID:
                element = By.ID
            case LocatorType.NAME:
                element = By.NAME
            case LocatorType.XPATH:
                element = By.XPATH
            case LocatorType.CLASS_NAME:
                element = By.CLASS_NAME
            case _:
                raise NotImplementedError(f"Locator type {locator_type} not implemented yet.")
        return element
