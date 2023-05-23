from enum import Enum, auto

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


class PetSpecies(Enum):
    FISH = auto()
    DOGS = auto()
    CATS = auto()
    REPTILES = auto()
    BIRDS = auto()


def __get_available_pets():
    return {
        "FISH": {
            "Angelfish": {"Large Angelfish": 16.50, "Small Angelfish": 16.50},
            "Tiger Shark": {"Toothless Tiger Shark": 18.50},
            "Koi": {"Spotted Koi": 18.50, "Spotless Koi": 18.50},
            "Goldfish": {"Adult Male Goldfish": 5.50, "Adult Female Goldfish": 5.29}
        },
        "DOGS": {
            "Bulldog": {"Male Adult Bulldog": 18.50, "Female Puppy Bulldog": 18.50},
            "Poodle": {"Male Puppy Poodle": 18.50},
            "Dalmation": {"Spotless Male Puppy Dalmation": 18.50, "Spotted Adult Female Dalmation": 18.50},
            "Golden Retriever": {"Adult Female Golden Retriever": 155.29},
            #  TODO: Update Labradors Data when Information is Updated (see Bug #007)
            "Labrador Retriever": {"Adult Male Labrador Retriever": "?", "Adult Female Labrador Retriever": "?"},
            "Chihuahua": {"Adult Male Chihuahua": 125.50, "Adult Female Chihuahua": 155.29}
        },
        "CATS": {
            "Manx": {"Tailless Manx": 58.50, "With tail Manx": 23.50},
            "Persian": {"Adult Female Persian": 93.50, "Adult Male Persian": 93.50}
        },
        "REPTILES": {
            "Rattlesnake": {"Venomless Rattlesnake": 18.50, "Rattleless Rattlesnake": 18.50},
            "Iguana": {"Green Adult Iguana": 18.50}
        },
        "BIRDS": {
            "Amazon Parrot": {"Adult Male Amazon Parrot": 193.50},
            "Finch": {"Adult Male Finch": 15.50}
        }
    }


def get_random_pet_breed_and_description():
    random_pet = random_data_generator.get_random_choice([pet.name for pet in PetSpecies])
    random_breed = random_data_generator.get_random_choice([breed for breed in __get_available_pets()[random_pet]])
    breed_data = __get_available_pets()[random_pet][random_breed]
    description = random_data_generator.get_random_choice([breed for breed in breed_data])
    price = breed_data[description]
    return random_pet, random_breed, description, price
