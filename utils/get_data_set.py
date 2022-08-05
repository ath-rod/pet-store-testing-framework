from json import dumps

from resources.random_data import *


def get_pet(photoUrls_amount=-1):
    pet_id = get_random_number()
    payload = dumps(
                {
                    "id": pet_id,
                    "category": {
                        "id": get_random_number(),
                        "name": get_random_name()
                    },
                    "name": get_random_name(),
                    "photoUrls": get_random_list_of_names(photoUrls_amount),
                    "tags": [
                        {
                            "id": get_random_number(),
                            "name": get_random_name()
                        }
                    ],
                    "status": get_random_element(["available", "pending", "sold"])
                }
            )
    return pet_id, payload
