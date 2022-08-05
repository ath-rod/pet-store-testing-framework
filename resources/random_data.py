import random

from faker import Faker

fake_data = Faker()


def get_random_name():
    return random.choice([fake_data.first_name(), fake_data.name()])


def get_random_list_of_names(amount=-1): #Find a more intuitive way to state you want a random amount
    if amount < 0: amount = random.randint(0, 10)
    list_of_names = []
    for i in range(amount):
        list_of_names.append(random.choice([fake_data.first_name(), fake_data.name()]))
    return list_of_names


def get_random_number(min_num=0, max_num=9999):
    return random.randint(min_num, max_num)


def get_random_element(options):
    return random.choice(options)
