import pytest
from assertpy import assert_that, soft_assertions
from requests import codes

from core.custom_assertions import assert_dicts_are_equal, assert_response_schema
from helpers.pet_wrapper import PetWrapper
from resources import random_data_generator
from utils.get_data_set import generate_pet
from utils.get_schema import get_pet_schema

wrapper = PetWrapper()


def test_add_pet():
    payload = {
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
    assert_response_schema(request.response.body_as_dict, get_pet_schema)
    assert_dicts_are_equal(request.payload, request.response.body_as_dict)

    response_get = wrapper.get_pet_by_id(request.response.body_as_dict['id'])
    assert_dicts_are_equal(request.response.body_as_dict, response_get.body_as_dict)


def test_get_pet():
    request_new_pet = wrapper.post_pet()
    response = wrapper.get_pet_by_id(request_new_pet.response.body_as_dict['id'])
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, get_pet_schema)
    assert_dicts_are_equal(request_new_pet.response.body_as_dict, response.body_as_dict)


def test_remove_pet():
    existing_pet = wrapper.post_pet()
    response = wrapper.delete_pet_by_id(existing_pet.response.body_as_dict['id'])
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_that(response.body_as_dict['message']).contains(str(existing_pet.response.body_as_dict['id']))

    response_get_deleted_pet = wrapper.get_pet_by_id(existing_pet.response.body_as_dict['id'])
    assert_that(response_get_deleted_pet.status_code).is_equal_to(codes.not_found)


def test_modify_pet():
    existing_pet = wrapper.post_pet()
    new_pet_data = generate_pet()
    new_pet_data['id'] = existing_pet.response.body_as_dict['id']

    response = wrapper.put_pet(new_pet_data)

    assert_that(response.status_code, f"{response.body_as_raw} {response.headers}").is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, get_pet_schema)
    assert_that(response.body_as_dict['id']).is_equal_to(existing_pet.response.body_as_dict['id'])
    assert_dicts_are_equal(response.body_as_dict, new_pet_data)


@pytest.mark.xfail(reason="Fails due to bug 001")
def test_add_empty_pet():
    request = wrapper.post_pet(payload={})
    with soft_assertions():
        assert_that(request.response.status_code, "Response code").is_equal_to(codes.bad_request)
        assert_that(request.response.body_as_dict).does_not_contain_key('id')


@pytest.mark.xfail(reason="Fails due to bug 002")
def test_add_already_existing_pet():
    existing_pet = wrapper.post_pet()
    new_pet_data = generate_pet()
    new_pet_data['id'] = existing_pet.response.body_as_dict['id']

    request = wrapper.post_pet(new_pet_data)
    actual_pet = wrapper.get_pet_by_id(existing_pet.response.body_as_dict['id'])

    with soft_assertions():
        assert_that(request.response.status_code, "Response code").is_equal_to(codes.bad_request)
        assert_response_schema(actual_pet.body_as_dict, get_pet_schema)
        assert_dicts_are_equal(existing_pet.response.body_as_dict, actual_pet.body_as_dict)


@pytest.mark.xfail(reason="Fails due to bug 003")
@pytest.mark.parametrize("invalid_status", random_data_generator.get_invalid_status_data(), ids=repr)
def test_modify_pet_with_invalid_status(invalid_status):
    existing_pet = wrapper.post_pet()
    expected_status = existing_pet.payload['status']
    payload_with_invalid_status = existing_pet.response.body_as_dict
    payload_with_invalid_status['status'] = invalid_status

    response = wrapper.put_pet(payload_with_invalid_status)

    actual_pet = wrapper.get_pet_by_id(existing_pet.response.body_as_dict['id'])
    actual_status = actual_pet.body_as_dict['status']

    with soft_assertions():
        assert_that(response.status_code, "Response code").is_equal_to(codes.bad_request)
        assert_response_schema(actual_pet.body_as_dict, get_pet_schema)
        assert_that(actual_status).is_equal_to(expected_status)
