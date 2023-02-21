import pytest
from assertpy import assert_that, soft_assertions
from requests import codes

from core.custom_assertions import assert_dicts_are_equal, assert_response_schema
from helpers.store_wrapper import StoreWrapper
from helpers.pet_wrapper import PetWrapper
from resources import random_data_generator
from utils.get_data_set import generate_order, generate_pet
from utils.custom_strings import parsed_date

store_wrapper = StoreWrapper()
pet_wrapper = PetWrapper()


def test_add_order(existing_pet_id):
    payload = {
        "id": random_data_generator.get_random_number(),
        "petId": existing_pet_id,
        "quantity": random_data_generator.get_random_number(),
        "shipDate": parsed_date(),
        "status": random_data_generator.get_random_element(["placed", "approved", "delivered"]),
        "complete": random_data_generator.get_random_bool()
    }
    request = store_wrapper.post_order(existing_pet_id, payload=payload)
    assert_that(request.response.status_code, request.response.body_as_raw).is_equal_to(codes.ok)
    assert_response_schema(request.response.body_as_dict, endpoint="store/order")
    assert_dicts_are_equal(request.payload, request.response.body_as_dict)

    response_get = store_wrapper.get_order_by_id(request.response.body_as_dict['id'])
    assert_dicts_are_equal(request.response.body_as_dict, response_get.body_as_dict)


def test_get_order(existing_pet_id):
    existing_order = store_wrapper.post_order(existing_pet_id)
    response = store_wrapper.get_order_by_id(existing_order.response.body_as_dict['id'])
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, endpoint="store/order")
    assert_dicts_are_equal(existing_order.response.body_as_dict, response.body_as_dict)


def test_remove_order(existing_pet_id):
    existing_order = store_wrapper.post_order(existing_pet_id)
    response = store_wrapper.delete_order_by_id(existing_order.response.body_as_dict['id'])
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_that(response.body_as_dict['message']).contains(str(existing_order.response.body_as_dict['id']))

    response_get_deleted_order = store_wrapper.get_order_by_id(existing_order.response.body_as_dict['id'])
    assert_that(response_get_deleted_order.status_code).is_equal_to(codes.not_found)


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_modify_order(existing_pet_id):
    existing_order = store_wrapper.post_order(existing_pet_id)
    new_order_data = generate_order(existing_pet_id, order_id=existing_order.response.body_as_dict['id'])

    response = store_wrapper.put_order(new_order_data)

    assert_that(response.status_code, f"{response.body_as_raw} {response.headers}").is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, endpoint="store/order")
    assert_that(response.body_as_dict['id']).is_equal_to(existing_order.response.body_as_dict['id'])
    assert_dicts_are_equal(response.body_as_dict, new_order_data)


def test_get_inventory():
    response = store_wrapper.get_store_inventory()
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, endpoint="store/inventory")
    assert_that(response.body_as_dict).contains("pending", "available", "sold")


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_add_oder_for_sold_pet():
    sold_pet_data = generate_pet()
    sold_pet_data['status'] = "sold"
    sold_pet = pet_wrapper.post_pet(sold_pet_data)

    request = store_wrapper.post_order(sold_pet.pet_id)
    assert_that(request.response.status_code, request.response.body_as_raw).is_equal_to(codes.bad_request)


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_e2e_order_process():
    available_pet_data = generate_pet()
    available_pet_data['status'] = "available"
    available_pet = pet_wrapper.post_pet(available_pet_data)
    previous_inventory = store_wrapper.get_store_inventory()

    order_payload = generate_order(available_pet.pet_id)
    order_payload['status'] = "placed"
    store_wrapper.post_order(available_pet.pet_id, order_payload)
    order_payload['status'] = "approved"
    store_wrapper.put_order(order_payload)
    order_payload['status'] = "delivered"
    delivered_order = store_wrapper.put_order(order_payload)

    actual_pet = pet_wrapper.get_pet_by_id(available_pet.pet_id)
    actual_inventory = store_wrapper.get_store_inventory()

    with soft_assertions():
        assert_that(delivered_order.response.body_as_dict['status'], "Order status").is_equal_to("delivered")
        assert_that(delivered_order.response.body_as_dict['complete'], "Order complete").is_true()
        assert_that(actual_pet.body_as_dict['status'], "Pet status").is_equal_to("sold")
        assert_that(actual_inventory.body_as_dict['sold'], "Inventory sold").is_equal_to(
            previous_inventory.body_as_dict['sold'] + 1)
        assert_that(actual_inventory.body_as_dict['available'], "Inventory available").is_equal_to(
            previous_inventory.body_as_dict['available'] - 1)


@pytest.fixture()
def existing_pet_id():
    existing_pet = pet_wrapper.post_pet()
    return existing_pet.pet_id
