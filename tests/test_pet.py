import requests
from assertpy import assert_that

from core.custom_assertions import assert_body_is_the_same
from helpers.pet_wrapper import PetWrapper

wrapper = PetWrapper()


def test_add_pet():  # TODO: explicit body (don't hide the test purpose)
    pet_id, response, expected = wrapper.create_pet()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_body_is_the_same(expected, response.body_as_dict)

    response_get = wrapper.get_pet_by_id(pet_id)
    assert_body_is_the_same(response.body_as_dict, response_get.body_as_dict)


def test_get_pet():
    pet_id, response_pet, _ = wrapper.create_pet()
    response = wrapper.get_pet_by_id(pet_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_body_is_the_same(response_pet.body_as_dict, response.body_as_dict)


def test_remove_pet():
    pet_id, response_pet, _ = wrapper.create_pet()
    response = wrapper.delete_pet_by_id(pet_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.body_as_dict['message']).contains(str(pet_id))

    response_get_deleted_pet = wrapper.get_pet_by_id(pet_id)
    assert_that(response_get_deleted_pet.status_code).is_equal_to(requests.codes.not_found)
