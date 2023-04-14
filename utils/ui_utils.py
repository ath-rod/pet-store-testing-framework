from enum import Enum, auto

from selenium.webdriver.common.by import By


class LocatorType(Enum):
    ID = auto()
    NAME = auto()
    XPATH = auto()


def find_element(driver, locator_type, locator):  # TODO: move this to enum itself
    match locator_type:
        case LocatorType.ID:
            element = driver.find_element(by=By.ID, value=locator)
        case LocatorType.NAME:
            element = driver.find_element(by=By.NAME, value=locator)
        case LocatorType.XPATH:
            element = driver.find_element(by=By.XPATH, value=locator)
        case _:
            raise NotImplementedError(f"Locator type {locator_type} not implemented yet.")
    return element
