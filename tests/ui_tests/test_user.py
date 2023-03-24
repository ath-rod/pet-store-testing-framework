from base_class_test import UIBaseClassTest
from core.custom_assertions import assert_that_element_is_present
from core.pages.sign_up import SignUpPage
from random_data_generator import get_random_number, get_random_string, get_random_name, get_random_email, \
    get_random_choice
from utils.ui_utils import LocatorType


class TestUser(UIBaseClassTest):
    def test_add_new_user(self):  # TODO: add improvement in report to include success message
        sign_up_page = SignUpPage(self.driver)
        user_id = get_random_string()
        password = get_random_string()
        favorite_category = get_random_choice(["FISH", "DOGS", "REPTILES", "CATS", "BIRDS"])

        sign_up_page.go_to_page()
        sign_up_page.user_id_input().send_keys(user_id)
        sign_up_page.password_input().send_keys(password)
        sign_up_page.repeat_password_input().send_keys(password)
        sign_up_page.first_name_input().send_keys(get_random_name())
        sign_up_page.last_name_input().send_keys(get_random_name())
        sign_up_page.email_input().send_keys(get_random_email())
        sign_up_page.phone_input().send_keys(get_random_number())
        sign_up_page.address_1_input().send_keys(get_random_string())
        sign_up_page.address_2_input().send_keys(get_random_string())
        sign_up_page.city_input().send_keys(get_random_string())
        sign_up_page.state_input().send_keys(get_random_string())
        sign_up_page.zip_input().send_keys(get_random_string())
        sign_up_page.country_input().send_keys(get_random_string())
        sign_up_page.language_preference_dropdown().select_option("english")
        sign_up_page.favourite_category_dropdown().select_option(favorite_category)
        sign_up_page.my_list_checkbox().click()
        sign_up_page.my_banner_checkbox().click()
        sign_up_page.save_account_button().click()

        assert_that_element_is_present(self.driver, LocatorType.ID, "Welcome", "Home Page")
