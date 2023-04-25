from driver import ChromeDriver
from core.pages.catalogs import PetBreedCatalogPage, PetDescriptionCatalogPage
from core.pages.checkout import CheckoutPage, ConfirmCheckoutInformationPage, OrderConfirmationPage
from core.pages.home import HomePage
from core.pages.pet_card import PetCardPage
from core.pages.shopping_cart import ShoppingCartPage
from core.pages.sign_in import SignInPage
from core.pages.sign_up import SignUpPage


class UIBaseClassTest:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = ChromeDriver()
        cls.driver = cls.driver.driver
        cls.home_page = HomePage(cls.driver)
        cls.sign_up_page = SignUpPage(cls.driver)
        cls.sign_in_page = SignInPage(cls.driver)
        cls.breed_catalog_page = PetBreedCatalogPage(cls.driver)
        cls.description_catalog_page = PetDescriptionCatalogPage(cls.driver)
        cls.shopping_cart_page = ShoppingCartPage(cls.driver)
        cls.checkout_page = CheckoutPage(cls.driver)
        cls.confirm_checkout_page = ConfirmCheckoutInformationPage(cls.driver)
        cls.order_confirmation_page = OrderConfirmationPage(cls.driver)
        cls.pet_card_page = PetCardPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
