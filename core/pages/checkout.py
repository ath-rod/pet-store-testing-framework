from config import UI_BASE_URI
from core.element import Element
from utils.ui_utils import LocatorType


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Order.action?newOrderForm=")

    def first_name_input(self):
        return Element(self.driver, LocatorType.NAME, "order.billToFirstName")

    def last_name_input(self):
        return Element(self.driver, LocatorType.NAME, "order.billToLastName")

    def main_address_input(self):
        return Element(self.driver, LocatorType.NAME, "order.billAddress1")

    def continue_button(self):
        return Element(self.driver, LocatorType.NAME, "newOrder")


class ConfirmCheckoutInformationPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Order.action")

    def confirm_button(self):
        return Element(self.driver, LocatorType.XPATH, "//a[contains(text(), 'Confirm')]")


class OrderConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Order.action?newOrder=&confirmed=true")

    def successful_order_message(self):
        return Element(self.driver, LocatorType.XPATH, "//ul['messages']/li")

    def first_name_bill_info(self):
        return Element(self.driver, LocatorType.XPATH,
                       "(//td[contains(text(), 'First name')])[1]/following-sibling::td")

    def last_name_bill_info(self):
        return Element(self.driver, LocatorType.XPATH, "(//td[contains(text(), 'Last name')])[1]/following-sibling::td")

    def address_bill_info(self):
        return Element(self.driver, LocatorType.XPATH,
                       "(//td[contains(text(), 'Address 1:')])[1]/following-sibling::td")

    def first_name_ship_info(self):
        return Element(self.driver, LocatorType.XPATH,
                       "(//td[contains(text(), 'First name')])[2]/following-sibling::td")

    def last_name_ship_info(self):
        return Element(self.driver, LocatorType.XPATH, "(//td[contains(text(), 'Last name')])[2]/following-sibling::td")

    def address_ship_info(self):
        return Element(self.driver, LocatorType.XPATH,
                       "(//td[contains(text(), 'Address 1:')])[2]/following-sibling::td")

    def pet_ordered_info(self, description):
        return Element(self.driver, LocatorType.XPATH, f"//td[normalize-space(text()) = '{description}']")

    def pet_quantity_info(self, description):
        return Element(self.driver, LocatorType.XPATH,
                       f"//td[normalize-space(text()) = '{description}']/following-sibling::td")

    def pet_price_info(self, description):
        return Element(self.driver, LocatorType.XPATH,
                       f"//td[normalize-space(text()) = '{description}']/following-sibling::td[2]")

    def pet_total_cost_info(self, description):
        return Element(self.driver, LocatorType.XPATH,
                       f"//td[normalize-space(text()) = '{description}']/following-sibling::td[3]")

    def order_total_info(self):
        return Element(self.driver, LocatorType.XPATH, "//th[contains(text(), 'Total:')]")
