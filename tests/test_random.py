from core.api_core import APIRequest
from assertpy import assert_that
from faker import Faker
from utils.get_data_set import get_pet
import requests
import random
from resources.random_data_generator import get_random_list_of_names

fake_data = Faker()
request = APIRequest()


def test_non_existing_pet():
    response = request.get('http://petstore.swagger.io/v2/pet/0')
    assert_that(response.status_code).is_equal_to(404)


def test_existing_pet():
    response = request.get('http://petstore.swagger.io/v2/pet/1000')
    assert_that(response.status_code).is_equal_to(200)


def test_connection_error():
    response = request.get('http://petstre.swagger.io/v2/pet/1234')
    assert_that(response.text).is_equal_to('ConnectionError')


def test_type():
    empty_dict = {}
    str1 = requests.get('https://httpbin.org/html')
    empty_dict = str1.json()
    print(empty_dict, type(empty_dict))


def test_names():
    print(get_pet())
    print(get_pet(0))


def test_random_list():
    random_list = random.sample([fake_data.first_name(), fake_data.name()], random.randint(0, 2))
    print(random_list)
    list_names = get_random_list_of_names(8)
    print(list_names)
