import requests

from helpers.pet_wrapper import PetWrapper
from core.custom_assertions import assert_body_is_the_same
from assertpy import assert_that

wrapper = PetWrapper()


def test_post_pet_op1():
    pet_id, response, expected = wrapper.create_pet()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_body_is_the_same(expected, response.as_dict)


def test_post_pet_op2():
    pet_id, response, expected = wrapper.create_pet()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_body_is_the_same(expected, response.as_dict)

    response_get = wrapper.get_pet_by_id(pet_id)
    assert_body_is_the_same(response.as_dict, response_get.as_dict)


def test_get_pet_by_id():
    pet_id, response_pet, _ = wrapper.create_pet()
    response = wrapper.get_pet_by_id(pet_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_body_is_the_same(response_pet.as_dict, response.as_dict)


def test_delete_pet_by_id():
    pet_id, response_pet, _ = wrapper.create_pet()
    response = wrapper.delete_pet_by_id(pet_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.as_dict['message']).contains(str(pet_id))

    response_get_deleted_pet = wrapper.get_pet_by_id(pet_id)
    assert_that(response_get_deleted_pet.status_code).is_equal_to(requests.codes.not_found)
