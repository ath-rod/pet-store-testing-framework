from json import dumps
from faker import Faker

import random

fake_data = Faker()


def get_pet():
    pet_id = random.randint(0, 9999)
    payload = dumps(
                {
                    "id": pet_id,
                    "category": {
                        "id": random.randint(0, 9999),
                        "name": fake_data.name()
                    },
                    "name": random.choice([fake_data.first_name(), fake_data.name()]),
                    "photoUrls": [
                        "Facha"
                    ],
                    "tags": [
                        {
                            "id": random.randint(0, 9999),
                            "name": random.choice([fake_data.first_name(), fake_data.name()])
                        }
                    ],
                    "status": random.choice(["available", "pending", "sold"])
                }
            )
    return pet_id, payload
