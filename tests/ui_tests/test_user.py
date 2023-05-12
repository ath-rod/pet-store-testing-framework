import pytest
from assertpy import assert_that

from base_class_test import UIBaseClassTest
from core.custom_assertions import assert_that_element_is_present
from resources.random_data_generator import get_random_number, get_random_string, get_random_name, get_random_email, \
    get_random_choice
from utils.get_data_set import PetSpecies


class TestUser(UIBaseClassTest):
    def test_add_new_user(self):  # TODO: add improvement in report to include success message
        user_id = get_random_string()
        password = get_random_string()
        favorite_category = get_random_choice([pet.name for pet in PetSpecies])

        self.sign_up_page.go_to_page()
        self.sign_up_page.user_id_input().clear_and_send_keys(user_id)
        self.sign_up_page.password_input().clear_and_send_keys(password)
        self.sign_up_page.repeat_password_input().clear_and_send_keys(password)
        self.sign_up_page.first_name_input().clear_and_send_keys(get_random_name())
        self.sign_up_page.last_name_input().clear_and_send_keys(get_random_name())
        self.sign_up_page.email_input().clear_and_send_keys(get_random_email())
        self.sign_up_page.phone_input().clear_and_send_keys(get_random_number())
        self.sign_up_page.address_1_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.address_2_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.city_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.state_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.zip_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.country_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.language_preference_dropdown().select_option("english")
        self.sign_up_page.favourite_category_dropdown().select_option(favorite_category)
        self.sign_up_page.my_list_checkbox().click()
        self.sign_up_page.my_banner_checkbox().click()
        self.sign_up_page.save_account_button().click()

        assert_that_element_is_present(self.home_page.distinctive_home_page_element(), page=self.home_page)

    def test_add_new_user_with_no_data(self):  # TODO: add improvement in report to include error message
        self.sign_up_page.go_to_page()
        clear_user_and_account_info(self.sign_up_page)
        self.sign_up_page.save_account_button().click()

        assert_that_element_is_present(self.sign_up_page.save_account_button(), self.sign_up_page)

    @pytest.mark.xfail(reason="Fails due to bug XXX")
    def test_add_new_user_with_no_account_information(self):
        self.sign_up_page.go_to_page()
        clear_user_and_account_info(self.sign_up_page)

        self.sign_up_page.user_id_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.password_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.repeat_password_input().clear_and_send_keys(get_random_string())
        self.sign_up_page.save_account_button().click()

        #  TODO: update test assertions after bug is fixed
        assert_that_element_is_present(self.sign_up_page.save_account_button(), self.sign_up_page)

    def test_sign_in_valid_user(self):
        user = self.random_user
        user.register_new_user()
        self.sign_in_page.go_to_page()

        self.sign_in_page.username_input().clear_and_send_keys(user.username)
        self.sign_in_page.password_input().clear_and_send_keys(user.password)
        self.sign_in_page.log_in_button().click()

        assert_that_element_is_present(self.home_page.distinctive_home_page_element(), self.home_page)
        assert_that_element_is_present(self.home_page.welcome_user_message(), self.home_page)
        welcome_message = self.home_page.welcome_user_message().get_text()
        assert_that(welcome_message).is_equal_to(f"Welcome {user.first_name}!")

    def test_sign_in_invalid_user(self):
        self.sign_in_page.go_to_page()

        self.sign_in_page.username_input().clear_and_send_keys(get_random_string())
        self.sign_in_page.password_input().clear_and_send_keys(get_random_string())
        self.sign_in_page.log_in_button().click()

        assert_that_element_is_present(self.sign_in_page.error_message(), self.sign_in_page)
        error_message = self.sign_in_page.error_message().get_text()
        assert_that(error_message).is_equal_to("Invalid username or password. Signon failed.")


def clear_user_and_account_info(sign_up_page):
    sign_up_page.user_id_input().clear()
    sign_up_page.password_input().clear()
    sign_up_page.repeat_password_input().clear()
    sign_up_page.first_name_input().clear()
    sign_up_page.last_name_input().clear()
    sign_up_page.email_input().clear()
    sign_up_page.phone_input().clear()
    sign_up_page.address_1_input().clear()
    sign_up_page.address_2_input().clear()
    sign_up_page.city_input().clear()
    sign_up_page.state_input().clear()
    sign_up_page.zip_input().clear()
    sign_up_page.country_input().clear()
