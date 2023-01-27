from assertpy import assert_that
from requests import codes

from core.custom_assertions import assert_body_is_the_same
from helpers.pet_wrapper import PetWrapper
from resources import random_data_generator
from utils.get_data_set import generate_pet

wrapper = PetWrapper()


def test_add_pet():
    payload = {
        "id": random_data_generator.get_random_number(),
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
    request = wrapper.post_pet(payload=payload)
    assert_that(request.response.status_code, request.response.body_as_raw).is_equal_to(codes.ok)
    assert_body_is_the_same(request.payload, request.response.body_as_dict)

    response_get = wrapper.get_pet_by_id(request.pet_id)
    assert_body_is_the_same(request.response.body_as_dict, response_get.body_as_dict)


def test_get_pet():
    request_new_pet = wrapper.post_pet()
    response = wrapper.get_pet_by_id(request_new_pet.pet_id)
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_body_is_the_same(request_new_pet.response.body_as_dict, response.body_as_dict)


def test_remove_pet():
    request_new_pet = wrapper.post_pet()
    response = wrapper.delete_pet_by_id(request_new_pet.pet_id)
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_that(response.body_as_dict['message']).contains(str(request_new_pet.pet_id))

    response_get_deleted_pet = wrapper.get_pet_by_id(request_new_pet.pet_id)
    assert_that(response_get_deleted_pet.status_code).is_equal_to(codes.not_found)


def test_modify_pet():  # TODO: keep investigating API as this test fails
    request_new_pet = wrapper.post_pet()
    new_pet_data = generate_pet(pet_id=request_new_pet.pet_id)  # TODO: should the explicit data be here?

    response = wrapper.put_pet_by_id(request_new_pet.pet_id, new_pet_data)

    assert_that(response.status_code, f"{response.body_as_raw} {response.headers}").is_equal_to(codes.ok)
    assert_that(response.body_as_dict['message']).contains(str(request_new_pet.pet_id))
    assert_body_is_the_same(response.body_as_dict, new_pet_data)
