from core.pages.sign_in import SignInPage
from core.pages.sign_up import SignUpPage
from resources.random_data_generator import get_random_number, get_random_string, get_random_name, get_random_email, \
    get_random_choice
from utils.get_data_set import PetSpecies


class RandomUser:
    def __init__(self, driver):
        self.driver = driver
        self.username = get_random_string()
        self.password = get_random_string()
        self.first_name = get_random_name()
        self.last_name = get_random_name()
        self.main_address = get_random_string()

    def register_new_user(self):
        sign_up_page = SignUpPage(self.driver)
        favorite_category = get_random_choice([pet.name for pet in PetSpecies])

        sign_up_page.go_to_page()
        sign_up_page.user_id_input().clear_and_send_keys(self.username)
        sign_up_page.password_input().clear_and_send_keys(self.password)
        sign_up_page.repeat_password_input().clear_and_send_keys(self.password)
        sign_up_page.first_name_input().clear_and_send_keys(self.first_name)
        sign_up_page.last_name_input().clear_and_send_keys(self.last_name)
        sign_up_page.email_input().clear_and_send_keys(get_random_email())
        sign_up_page.phone_input().clear_and_send_keys(get_random_number())
        sign_up_page.address_1_input().clear_and_send_keys(self.main_address)
        sign_up_page.address_2_input().clear_and_send_keys(get_random_string())
        sign_up_page.city_input().clear_and_send_keys(get_random_string())
        sign_up_page.state_input().clear_and_send_keys(get_random_string())
        sign_up_page.zip_input().clear_and_send_keys(get_random_string())
        sign_up_page.country_input().clear_and_send_keys(get_random_string())
        sign_up_page.language_preference_dropdown().select_option("english")
        sign_up_page.favourite_category_dropdown().select_option(favorite_category)
        sign_up_page.my_list_checkbox().click()
        sign_up_page.my_banner_checkbox().click()
        sign_up_page.save_account_button().click()

    def log_in_random_user(self):
        self.register_new_user()
        sign_in_page = SignInPage(self.driver)
        sign_in_page.go_to_page()
        sign_in_page.username_input().clear_and_send_keys(self.username)
        sign_in_page.password_input().clear_and_send_keys(self.password)
        sign_in_page.log_in_button().click()
