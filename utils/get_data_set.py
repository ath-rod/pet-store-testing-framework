from resources import random_data_generator


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
        # TODO: consider changing strings as names
        "photoUrls": random_data_generator.get_random_list_of_names(),
        "tags": [
            {
                "id": random_data_generator.get_random_number(),
                "name": random_data_generator.get_random_name()
            }
        ],
        "status": random_data_generator.get_random_element(["available", "pending", "sold"])
    }
    return payload
