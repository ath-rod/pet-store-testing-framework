from config import UI_BASE_URI, logger
from core.pages.checkout import CheckoutPage
from core.pages.confirm_checkout_information import ConfirmCheckoutInformationPage
from core.pages.home import HomePage
from core.pages.order_confirmation import OrderConfirmationPage
from core.pages.pet_breed_catalog import PetBreedCatalogPage
from core.pages.pet_card import PetCardPage
from core.pages.pet_description_catalog import PetDescriptionCatalogPage
from core.pages.shopping_cart import ShoppingCartPage
from core.pages.sign_in import SignInPage
from core.pages.sign_up import SignUpPage
from helpers.ui_helpers import RandomUser
from resources.driver import ChromeDriver


class UIBaseClassTest:
    __driver = None

    @classmethod
    def setup_class(cls):
        cls.__driver = ChromeDriver()
        cls.__driver = cls.__driver.driver
        cls.home_page = HomePage(cls.__driver)
        cls.sign_up_page = SignUpPage(cls.__driver)
        cls.sign_in_page = SignInPage(cls.__driver)
        cls.breed_catalog_page = PetBreedCatalogPage(cls.__driver)
        cls.description_catalog_page = PetDescriptionCatalogPage(cls.__driver)
        cls.shopping_cart_page = ShoppingCartPage(cls.__driver)
        cls.checkout_page = CheckoutPage(cls.__driver)
        cls.confirm_checkout_page = ConfirmCheckoutInformationPage(cls.__driver)
        cls.order_confirmation_page = OrderConfirmationPage(cls.__driver)
        cls.pet_card_page = PetCardPage(cls.__driver)
        cls.random_user = RandomUser(cls.__driver)

    @classmethod
    def teardown_class(cls):
        cls.__driver.quit()

    def go_to_sign_off_page(self):
        self.__driver.get(f"{UI_BASE_URI}/Account.action?signoff=")
        logger.info("Signed off")
