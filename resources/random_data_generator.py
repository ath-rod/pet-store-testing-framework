import random

from faker import Faker

fake_data = Faker()


# region General Data Generator

def get_random_bool():
    return fake_data.boolean()


def get_random_number(min_num=0, max_num=9999):
    return random.randint(min_num, max_num)


def get_random_element(options):
    return random.choice(options)


def get_random_name():
    return random.choice([fake_data.first_name(), fake_data.name()])


def get_random_list_of_names(quantity=get_random_number(max_num=30)):
    list_of_names = [random.choice([fake_data.first_name(), fake_data.name()]) for _ in range(quantity)]
    return list_of_names


def get_random_list_of_strings(quantity=get_random_number(max_num=30)):
    list_of_strings = [fake_data.pystr() for _ in range(quantity)]
    return list_of_strings


# endregion


# region API Data Generator
def get_invalid_status_data():
    yield fake_data.random_int()
    yield fake_data.random_int() * -1
    yield fake_data.random_number(digits=fake_data.random_int(min=10, max=20))
    yield fake_data.pyfloat()
    yield fake_data.pystr()
    yield fake_data.password(special_chars=True)
    yield fake_data.boolean()
# endregion
