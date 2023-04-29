from config import UI_BASE_URI
from core.element import Element
from utils.ui_utils import LocatorType


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(f"{UI_BASE_URI}/Account.action?newAccountForm=")

    def user_id_input(self):
        return Element(self.driver, LocatorType.NAME, "username")

    def password_input(self):
        return Element(self.driver, LocatorType.NAME, "password")

    def repeat_password_input(self):
        return Element(self.driver, LocatorType.NAME, "repeatedPassword")

    def first_name_input(self):
        return Element(self.driver, LocatorType.NAME, "account.firstName")

    def last_name_input(self):
        return Element(self.driver, LocatorType.NAME, "account.lastName")

    def email_input(self):
        return Element(self.driver, LocatorType.NAME, "account.email")

    def phone_input(self):
        return Element(self.driver, LocatorType.NAME, "account.phone")

    def address_1_input(self):
        return Element(self.driver, LocatorType.NAME, "account.address1")

    def address_2_input(self):
        return Element(self.driver, LocatorType.NAME, "account.address2")

    def city_input(self):
        return Element(self.driver, LocatorType.NAME, "account.city")

    def state_input(self):
        return Element(self.driver, LocatorType.NAME, "account.state")

    def zip_input(self):
        return Element(self.driver, LocatorType.NAME, "account.zip")

    def country_input(self):
        return Element(self.driver, LocatorType.NAME, "account.country")

    def language_preference_dropdown(self):
        return Element(self.driver, LocatorType.NAME, "account.languagePreference")

    def favourite_category_dropdown(self):
        return Element(self.driver, LocatorType.NAME, "account.favouriteCategoryId")

    def my_list_checkbox(self):
        return Element(self.driver, LocatorType.NAME, "account.listOption")

    def my_banner_checkbox(self):
        return Element(self.driver, LocatorType.NAME, "account.bannerOption")

    def save_account_button(self):
        return Element(self.driver, LocatorType.NAME, "newAccount")
