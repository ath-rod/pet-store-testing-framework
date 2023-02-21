from resources import random_data_generator
from utils.custom_strings import parsed_date


def generate_pet(pet_id=None):
    if pet_id is None:
        pet_id = random_data_generator.get_random_number()
    payload = {
        "id": pet_id,
        "category": {
            "id": random_data_generator.get_random_number(),
            "name": random_data_generator.get_random_name()
        },
        "name": random_data_generator.get_random_name(),
        "photoUrls": random_data_generator.get_random_list_of_strings(),
        "tags": [
            {
                "id": random_data_generator.get_random_number(),
                "name": random_data_generator.get_random_name()
            }
        ],
        "status": random_data_generator.get_random_element(["available", "pending", "sold"])
    }
    return payload


def generate_order(pet_id, order_id=None):
    if order_id is None:
        order_id = random_data_generator.get_random_number()
    payload = {
        "id": order_id,
        "petId": pet_id,
        "quantity": random_data_generator.get_random_number(),
        "shipDate": parsed_date(),
        "status": random_data_generator.get_random_element(["placed", "approved", "delivered"]),
        "complete": random_data_generator.get_random_bool()
    }
    return payload
