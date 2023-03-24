from resources import random_data_generator
from utils.custom_strings import parsed_date


def generate_pet():
    payload = {
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
        "status": random_data_generator.get_random_choice(["available", "pending", "sold"])
    }
    return payload


def generate_order(pet_id):
    payload = {
        "petId": pet_id,
        "quantity": random_data_generator.get_random_number(),
        "shipDate": parsed_date(),
        "status": random_data_generator.get_random_choice(["placed", "approved", "delivered"]),
        "complete": random_data_generator.get_random_bool()
    }
    return payload
