from json import dumps

from resources import random_data_generator


def get_pet():
    pet_id = random_data_generator.get_random_number()
    payload = dumps(
        {
            "id": pet_id,
            "category": {
                "id": random_data_generator.get_random_number(),
                "name": random_data_generator.get_random_name()
            },
            "name": random_data_generator.get_random_name(),
            "photoUrls": random_data_generator.get_random_list_of_names(),
            "tags": [
                {
                    "id": random_data_generator.get_random_number(),
                    "name": random_data_generator.get_random_name()
                }
            ],
            "status": random_data_generator.get_random_element(["available", "pending", "sold"])
        }
    )
    return pet_id, payload
