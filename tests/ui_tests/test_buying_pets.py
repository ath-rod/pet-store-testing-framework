import pytest
from assertpy import soft_assertions, assert_that

from base_class_test import UIBaseClassTest
from core.custom_assertions import assert_that_element_is_present, assert_that_element_is_not_present
from random_data_generator import get_random_number
from utils.custom_strings import get_number_from_price_string
from utils.get_data_set import get_random_pet_breed_and_description


class TestBuyPet(UIBaseClassTest):
    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.random_user.log_in_random_user()

    @pytest.fixture()
    def sign_out_setup_sign_in_teardown(self):
        self.go_to_sign_off_page()
        yield
        self.random_user.log_in_random_user()

    @pytest.mark.parametrize("pet, breed, description, price", [get_random_pet_breed_and_description()])
    def test_e2e_buy_one_random_pet_from_sidebar_and_catalog_cart_button(self, pet, breed, description, price):
        if breed == "Labrador Retriever":
            pytest.skip(reason="Bug XXX")
        expected_pet_quantity = get_random_number()

        self.home_page.go_to_page()
        self.home_page.sidebar_pet_option(pet).click()
        self.breed_catalog_page.pet_breed(breed).click()
        self.description_catalog_page.pet_add_to_cart_button(description).click()
        self.shopping_cart_page.quantity_input(description).clear_and_send_keys(expected_pet_quantity).press_enter()
        self.shopping_cart_page.checkout_button().click()
        self.checkout_page.continue_button().click()
        self.confirm_checkout_page.confirm_button().click()
        success_message = self.order_confirmation_page.successful_order_message().get_text()
        actual_first_name_bill = self.order_confirmation_page.first_name_bill_info().get_text()
        actual_last_name_bill = self.order_confirmation_page.last_name_bill_info().get_text()
        actual_main_address_bill = self.order_confirmation_page.address_bill_info().get_text()
        actual_first_name_ship = self.order_confirmation_page.first_name_ship_info().get_text()
        actual_last_name_ship = self.order_confirmation_page.last_name_ship_info().get_text()
        actual_main_address_ship = self.order_confirmation_page.address_ship_info().get_text()

        with soft_assertions():
            assert_that(success_message).is_equal_to("Thank you, your order has been submitted.")
            assert_that(actual_first_name_bill, "Bill: First name").is_equal_to(self.random_user.first_name)
            assert_that(actual_last_name_bill, "Bill: Last name").is_equal_to(self.random_user.last_name)
            assert_that(actual_main_address_bill, "Bill: Main address").is_equal_to(self.random_user.main_address)
            assert_that(actual_first_name_ship, "Ship: First name").is_equal_to(self.random_user.first_name)
            assert_that(actual_last_name_ship, "Ship: Last name").is_equal_to(self.random_user.last_name)
            assert_that(actual_main_address_ship, "Ship: Main address").is_equal_to(self.random_user.main_address)

    @pytest.mark.parametrize("pet, breed, description, price", [get_random_pet_breed_and_description()])
    def test_e2e_buy_random_pet_from_top_bar_and_card_cart_button(self, pet, breed, description, price):
        if breed == "Labrador Retriever":
            pytest.skip(reason="Fails due to bug XXX")
        expected_pet_quantity = get_random_number()
        expected_total = expected_pet_quantity * price

        self.home_page.go_to_page()
        self.home_page.top_bar_pet_option(pet).click()
        self.breed_catalog_page.pet_breed(breed).click()
        self.description_catalog_page.pet_item_id(description).click()
        self.pet_card_page.add_to_cart_button().click()
        self.shopping_cart_page.quantity_input(description).clear_and_send_keys(expected_pet_quantity).press_enter()
        self.shopping_cart_page.checkout_button().click()
        self.checkout_page.continue_button().click()
        self.confirm_checkout_page.confirm_button().click()
        success_message = self.order_confirmation_page.successful_order_message().get_text()
        actual_pet_ordered = self.order_confirmation_page.pet_ordered_info(description).get_text()
        actual_pet_quantity = self.order_confirmation_page.pet_quantity_info(description).get_text()
        actual_pet_price = self.order_confirmation_page.pet_price_info(description).get_text()
        actual_pet_total_cost = self.order_confirmation_page.pet_total_cost_info(description).get_text()
        actual_order_total = self.order_confirmation_page.order_total_info().get_text()

        with soft_assertions():
            assert_that(success_message).is_equal_to("Thank you, your order has been submitted.")
            assert_that(actual_pet_ordered, "Pet Ordered").is_equal_to(description)
            assert_that(int(actual_pet_quantity), "Pet Quantity").is_equal_to(expected_pet_quantity)
            assert_that(get_number_from_price_string(actual_pet_price), "Pet Price").is_equal_to(price)
            assert_that(get_number_from_price_string(actual_pet_total_cost), "Pet Total").is_equal_to(expected_total)
            assert_that(get_number_from_price_string(actual_order_total), "Order Total").is_equal_to(expected_total)

    @pytest.mark.parametrize("pet, breed, description, price", [get_random_pet_breed_and_description()])
    @pytest.mark.xfail(reason="Fails due to bug XXX")
    def test_skip_order_confirmation(self, pet, breed, description, price):
        self.home_page.go_to_page()
        self.home_page.top_bar_pet_option(pet).click()
        self.breed_catalog_page.pet_breed(breed).click()
        self.description_catalog_page.pet_add_to_cart_button(description).click()
        self.shopping_cart_page.checkout_button().click()
        self.order_confirmation_page.go_to_page()
        #  TODO: add assertion for error message after bug is fixed
        self.shopping_cart_page.go_to_page()
        assert_that_element_is_present(self.shopping_cart_page.pet_description_info(description),
                                       self.shopping_cart_page)

    @pytest.mark.parametrize("invalid_quantity", [0, get_random_number(min_num=-9999, max_num=-1)])
    @pytest.mark.parametrize("pet, breed, description, price", [get_random_pet_breed_and_description()])
    @pytest.mark.skip(reason="Fails due to bug XXX")
    def test_buy_invalid_pet_quantity(self, pet, breed, description, price, invalid_quantity):
        self.home_page.go_to_page()
        self.home_page.sidebar_pet_option(pet).click()
        self.breed_catalog_page.pet_breed(breed).click()
        self.description_catalog_page.pet_add_to_cart_button(description).click()
        self.shopping_cart_page.quantity_input(description).clear_and_send_keys(invalid_quantity).press_enter()
        assert_that_element_is_present(self.shopping_cart_page.empty_cart_message(), self.shopping_cart_page)
        assert_that_element_is_not_present(self.shopping_cart_page.checkout_button(), self.shopping_cart_page)

    @pytest.mark.parametrize("pet, breed, description, price", [get_random_pet_breed_and_description()])
    def test_checkout_without_being_logged_in(self, pet, breed, description, price, sign_out_setup_sign_in_teardown):
        self.home_page.go_to_page()
        self.home_page.sidebar_pet_option(pet).click()
        self.breed_catalog_page.pet_breed(breed).click()
        self.description_catalog_page.pet_add_to_cart_button(description).click()
        self.shopping_cart_page.checkout_button().click()
        assert_that_element_is_present(self.shopping_cart_page.not_logged_in_error_message(), self.shopping_cart_page)
        error_message = self.shopping_cart_page.not_logged_in_error_message().get_text()
        assert_that(error_message).is_equal_to(
            "You must sign on before attempting to check out. Please sign on and try checking out again.")
