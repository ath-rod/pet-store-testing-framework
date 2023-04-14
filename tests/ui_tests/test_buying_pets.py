import time

import pytest
from assertpy import assert_that
from utils.get_data_set import get_random_pet_breed_and_description
from base_class_test import UIBaseClassTest
from core.custom_assertions import assert_that_element_is_present
from core.pages.home import HomePage
from core.pages.catalogs import PetBreedCatalogPage, PetDescriptionCatalogPage
from core.pages.shopping_cart import ShoppingCartPage
from core.pages.sign_in import SignInPage
from core.pages.sign_up import SignUpPage
from helpers.ui_helpers import RandomUser
from utils.get_data_set import PetSpecies
from random_data_generator import get_random_number, get_random_string, get_random_name, get_random_email, \
    get_random_choice
from utils.ui_utils import LocatorType


class TestBuyPet(UIBaseClassTest):  # Can it be
    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.random_user = RandomUser(cls.driver)
        cls.random_user.log_in_random_user()
        cls.home_page = HomePage(cls.driver)
        cls.breed_catalog_page = PetBreedCatalogPage(cls.driver)
        cls.description_catalog_page = PetDescriptionCatalogPage(cls.driver)
        cls.shopping_cart_page = ShoppingCartPage(cls.driver)

    def test_e2e_buy_random_pet_option_1(self):  # TODO: rename or add description instead of "option 1"
        pet, breed, description = get_random_pet_breed_and_description()

        self.home_page.go_to_page()
        self.home_page.sidebar_pet_option(pet).click()
        self.breed_catalog_page.pet_breed(breed).click()
        self.description_catalog_page.pet_add_to_cart_button(description).click()
        # self.shopping_cart_page.quantity_input().clear_and_send_keys(get_random_number())
        self.shopping_cart_page.checkout_button().click()
        #

        time.sleep(5)




