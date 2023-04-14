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


def __get_available_pets(species):
    match species:
        case PetSpecies.FISH.name:
            return {
                "Angelfish": ["Large Angelfish", "Small Angelfish"],
                "Tiger Shark": ["Toothless Tiger Shark"],
                "Koi": ["Spotted Koi", "Spotless Koi"],
                "Goldfish": ["Adult Male Goldfish", "Adult Female Goldfish"]
            }
        case PetSpecies.DOGS.name:
            return {
                "Bulldog": ["Male Adult Bulldog", "Female Puppy Bulldog"],
                "Poodle": ["Male Puppy Poodle"],
                "Dalmation": ["Spotless Male Puppy Dalmation", "Spotted Adult Female Dalmation"],
                "Golden Retriever": ["Adult Female Golden Retriever"],
                #  TODO: add to report data for labrador retrievers is repeated
                "Labrador Retriever": ["Adult Male Labrador Retriever", "Adult Female Labrador Retriever"],
                "Chihuahua": ["Adult Male Chihuahua", "Adult Female Chihuahua"]
            }
        case PetSpecies.CATS.name:
            return {
                "Manx": ["Tailless Manx", "With tail Manx"],
                "Persian": ["Adult Female Persian", "Adult Male Persian"]
            }
        case PetSpecies.REPTILES.name:
            return {
                "Rattlesnake": ["Venomless Rattlesnake", "Rattleless Rattlesnake"],
                "Iguana": ["Green Adult Iguana"]
            }
        case PetSpecies.BIRDS.name:
            return {
                "Amazon Parrot": ["Adult Male Amazon Parrot"],
                "Finch": ["Adult Male Finch"]
            }


def get_random_pet_breed_and_description():
    random_pet = random_data_generator.get_random_choice([pet.name for pet in PetSpecies])
    pet_options = __get_available_pets(random_pet)
    random_breed = random_data_generator.get_random_choice([breed for breed in pet_options])
    description = random_data_generator.get_random_choice(pet_options[random_breed])
    return random_pet, random_breed, description
