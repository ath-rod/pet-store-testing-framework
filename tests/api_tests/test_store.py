import pytest
from assertpy import assert_that, soft_assertions
from requests import codes

from core.custom_assertions import assert_dicts_are_equal, assert_response_schema
from helpers.pet_wrapper import PetWrapper
from helpers.store_wrapper import StoreWrapper
from resources import random_data_generator
from utils.custom_strings import parsed_date
from utils.get_data_set import generate_order, generate_pet
from utils.get_schema import get_store_order_schema, get_store_inventory_schema

store_wrapper = StoreWrapper()
pet_wrapper = PetWrapper()


def test_add_order(existing_pet_id):
    payload = {
        "id": random_data_generator.get_random_number(),
        "petId": existing_pet_id,
        "quantity": random_data_generator.get_random_number(),
        "shipDate": parsed_date(),
        "status": random_data_generator.get_random_choice(["placed", "approved", "delivered"]),
        "complete": random_data_generator.get_random_bool()
    }
    request = store_wrapper.post_order(existing_pet_id, payload=payload)
    assert_that(request.response.status_code, request.response.body_as_raw).is_equal_to(codes.ok)
    assert_response_schema(request.response.body_as_dict, get_store_order_schema)
    assert_dicts_are_equal(request.payload, request.response.body_as_dict)

    response_get = store_wrapper.get_order_by_id(request.response.body_as_dict['id'])
    assert_dicts_are_equal(request.response.body_as_dict, response_get.body_as_dict)


@pytest.mark.skip(reason="Fails inconsistently due to Bug XXX")
def test_get_order(existing_pet_id):
    existing_order = store_wrapper.post_order(existing_pet_id)
    response = store_wrapper.get_order_by_id(existing_order.response.body_as_dict['id'])
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, get_store_order_schema)
    assert_dicts_are_equal(existing_order.response.body_as_dict, response.body_as_dict)


@pytest.mark.skip("Fails inconsistently due to Bug XXX")
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
    new_order_data = {"id": existing_order.response.body_as_dict['id']}
    new_order_data.update(generate_order(existing_pet_id))

    response = store_wrapper.put_order(new_order_data)

    assert_that(response.status_code, f"{response.body_as_raw} {response.headers}").is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, get_store_order_schema)
    assert_that(response.body_as_dict['id']).is_equal_to(existing_order.response.body_as_dict['id'])
    assert_dicts_are_equal(response.body_as_dict, new_order_data)


def test_get_inventory():
    response = store_wrapper.get_store_inventory()
    assert_that(response.status_code, response.body_as_raw).is_equal_to(codes.ok)
    assert_response_schema(response.body_as_dict, get_store_inventory_schema, allow_unknown=True)
    assert_that(response.body_as_dict).contains("pending", "available", "sold")


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_add_order_for_0_pets(existing_pet_id):
    new_order = generate_order(existing_pet_id)
    new_order['quantity'] = 0

    request = store_wrapper.post_order(existing_pet_id, payload=new_order)
    assert_that(request.response.status_code, request.response.body_as_raw).is_equal_to(codes.bad_request)


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_add_order_for_sold_pet():
    sold_pet_data = generate_pet()
    sold_pet_data['status'] = "sold"
    sold_pet = pet_wrapper.post_pet(sold_pet_data)

    request = store_wrapper.post_order(sold_pet.response.body_as_dict['id'])
    assert_that(request.response.status_code, request.response.body_as_raw).is_equal_to(codes.bad_request)


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_add_empty_order(existing_pet_id):
    request = store_wrapper.post_order(existing_pet_id, payload={})
    with soft_assertions():
        assert_that(request.response.status_code, "Response code").is_equal_to(codes.bad_request)
        assert_that(request.response.body_as_dict).does_not_contain_key('id')


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_add_already_existing_order(existing_pet_id):
    existing_order = store_wrapper.post_order(existing_pet_id)
    new_order = generate_order(existing_pet_id)
    new_order['id'] = existing_order.response.body_as_dict['id']

    request = store_wrapper.post_order(existing_pet_id, payload=new_order)
    actual_order = store_wrapper.get_order_by_id(existing_order.response.body_as_dict['id'])

    with soft_assertions():
        assert_that(request.response.status_code, "Response code").is_equal_to(codes.bad_request)
        assert_response_schema(actual_order.body_as_dict, get_store_order_schema)
        assert_dicts_are_equal(existing_order.response.body_as_dict, actual_order.body_as_dict)


@pytest.mark.xfail(reason="Fails due to bug #00X")
@pytest.mark.parametrize("invalid_status", random_data_generator.get_invalid_status_data(), ids=repr)
def test_modify_order_with_invalid_status(invalid_status, existing_pet_id):
    existing_order = store_wrapper.post_order(existing_pet_id)
    expected_status = existing_order.payload['status']
    payload_with_invalid_status = existing_order.response.body_as_dict
    payload_with_invalid_status['status'] = invalid_status

    response = store_wrapper.put_order(payload_with_invalid_status)

    actual_order = store_wrapper.get_order_by_id(existing_order.response.body_as_dict['id'])
    actual_status = actual_order.body_as_dict['status']

    with soft_assertions():
        assert_that(response.status_code, "Response code").is_equal_to(codes.bad_request)
        assert_response_schema(actual_order.body_as_dict, get_store_order_schema)
        assert_that(actual_status).is_equal_to(expected_status)


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_order_id_is_generated(existing_pet_id):
    new_order = {"id": random_data_generator.get_random_number()}
    new_order.update(generate_order(existing_pet_id))

    request = store_wrapper.post_order(existing_pet_id, payload=new_order)
    get_order = store_wrapper.get_order_by_id(new_order['id'])

    with soft_assertions():
        assert_that(request.response.status_code, "Post order response code").is_equal_to(codes.ok)
        assert_that(get_order.status_code, "Get order response code").is_equal_to(codes.bad_request)
        assert_that(request.response.body_as_dict['id'], "ID").is_not_equal_to(new_order['id'])


@pytest.mark.xfail(reason="Fails due to bug #00X")
def test_e2e_order_process():
    available_pet_data = generate_pet()
    available_pet_data['status'] = "available"
    available_pet = pet_wrapper.post_pet(available_pet_data)
    previous_inventory = store_wrapper.get_store_inventory()

    order_payload = generate_order(available_pet.response.body_as_dict['id'])
    order_payload['status'] = "placed"
    store_wrapper.post_order(available_pet.response.body_as_dict['id'], order_payload)
    order_payload['status'] = "approved"
    store_wrapper.put_order(order_payload)
    order_payload['status'] = "delivered"
    delivered_order = store_wrapper.put_order(order_payload)

    actual_pet = pet_wrapper.get_pet_by_id(available_pet.response.body_as_dict['id'])
    actual_inventory = store_wrapper.get_store_inventory()

    with soft_assertions():
        assert_that(delivered_order.body_as_dict['status'], "Order status").is_equal_to("delivered")
        assert_that(delivered_order.body_as_dict['complete'], "Order complete").is_true()
        assert_that(actual_pet.body_as_dict['status'], "Pet status").is_equal_to("sold")
        assert_that(actual_inventory.body_as_dict['sold'], "Inventory sold").is_equal_to(
            previous_inventory.body_as_dict['sold'] + 1)
        assert_that(actual_inventory.body_as_dict['available'], "Inventory available").is_equal_to(
            previous_inventory.body_as_dict['available'] - 1)


@pytest.fixture()
def existing_pet_id():
    existing_pet = pet_wrapper.post_pet()
    return existing_pet.response.body_as_dict['id']
