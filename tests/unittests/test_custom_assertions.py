from random import shuffle

from faker import Faker
from pytest import raises

from resources.random_data_generator import fake_data
from utils.get_data_set import generate_pet, generate_order
from assertpy import soft_assertions
from core.custom_assertions import assert_dicts_are_equal, assert_response_schema

fake_data = Faker()


class TestAssertDictsAreEqual:
    nested_dict_a = fake_data.pydict(value_types=dict)
    nested_dict_b = fake_data.pydict(value_types=dict)

    def test_same_nested_dicts(self):
        assert_dicts_are_equal(self.nested_dict_a, self.nested_dict_a.copy())

    def test_different_nested_dicts(self):
        """ As they are randomly generated they mostly test Actual dict doesn't contain[key]"""
        with raises(AssertionError):
            assert_dicts_are_equal(self.nested_dict_a, self.nested_dict_b)

    def test_same_nested_dicts_different_order(self):
        dict_keys = list(self.nested_dict_a.keys())
        shuffle(dict_keys)
        shuffled_dict = {}
        for key in dict_keys:
            shuffled_dict.update({key: self.nested_dict_a[key]})
        assert_dicts_are_equal(self.nested_dict_a, shuffled_dict)

    def test_similar_nested_dicts(self):
        """ As they are similar they mostly test Expected x to be equal to y"""
        with raises(AssertionError):
            assert_dicts_are_equal(self.nested_dict_a, get_similar_dict(self.nested_dict_a))

    def test_lists_only_in_actual_dict(self):
        with raises(AssertionError):
            assert_dicts_are_equal(self.nested_dict_a, get_dict_with_dicts_inside_some_lists())

    def test_lists_only_in_expected_dict(self):
        with raises(AssertionError):
            assert_dicts_are_equal(get_dict_with_dicts_inside_some_lists(), self.nested_dict_a)

    def test_same_dicts_with_dicts_in_lists(self):
        dict_with_dicts_inside_lists = get_dict_with_dicts_inside_some_lists()
        assert_dicts_are_equal(dict_with_dicts_inside_lists, dict_with_dicts_inside_lists.copy())

    def test_different_dicts_with_dicts_in_lists(self):
        with raises(AssertionError):
            dict_with_dicts_inside_lists = get_dict_with_dicts_inside_some_lists()
            assert_dicts_are_equal(dict_with_dicts_inside_lists, get_similar_dict(dict_with_dicts_inside_lists))


def get_similar_dict(dict_to_copy):
    similar_dict = dict_to_copy.copy()
    random_keys = fake_data.random_choices(dict_to_copy.keys())
    for key in random_keys:
        similar_dict[key] = fake_data.random_element(fake_data.pylist())
    return similar_dict


def get_dict_with_dicts_inside_some_lists():
    dict_with_dicts_inside_lists = fake_data.pydict(value_types=[dict, list])
    lists_in_dict = [key for key in dict_with_dicts_inside_lists if isinstance(dict_with_dicts_inside_lists[key], list)]
    dict_random_lists = fake_data.random_choices(lists_in_dict)
    for key in dict_random_lists:
        dict_with_dicts_inside_lists[key].append(fake_data.pydict())
    return dict_with_dicts_inside_lists


class TestAssertSchema:
    valid_pet_schema = generate_pet()
    valid_order_schema = generate_order(fake_data.random_int())
    valid_inventory_schema = {
        'available': fake_data.random_int(),
        'pending': fake_data.random_int(),
        'sold': fake_data.random_int(),
        'random': fake_data.random_int()
    }
    pet_endpoint = "pet"
    order_endpoint = "store/order"
    inventory_endpoint = "store/inventory"

    def test_valid_schema(self):
        with soft_assertions():
            assert_response_schema(self.valid_pet_schema, endpoint=self.pet_endpoint)
            assert_response_schema(self.valid_order_schema, endpoint=self.order_endpoint)
            assert_response_schema(self.valid_inventory_schema, endpoint=self.inventory_endpoint)

    def test_random_invalid_dict(self):
        with raises(AssertionError):
            with soft_assertions():
                assert_response_schema(fake_data.pydict(value_types=dict), endpoint=self.pet_endpoint)
                assert_response_schema(fake_data.pydict(value_types=dict), endpoint=self.order_endpoint)
                assert_response_schema(fake_data.pydict(value_types=dict), endpoint=self.inventory_endpoint)

    def test_incomplete_schema(self):
        with raises(AssertionError):
            with soft_assertions():
                assert_response_schema(get_incomplete_dict(self.valid_pet_schema), endpoint=self.pet_endpoint)
                assert_response_schema(get_incomplete_dict(self.valid_order_schema), endpoint=self.order_endpoint)
                assert_response_schema(get_incomplete_dict(self.valid_inventory_schema),
                                       endpoint=self.inventory_endpoint)

    def test_empty_schema(self):
        with raises(AssertionError):
            with soft_assertions():
                assert_response_schema({}, endpoint=self.pet_endpoint)
                assert_response_schema({}, endpoint=self.order_endpoint)
                assert_response_schema({}, endpoint=self.inventory_endpoint)

    def test_invalid_type_boolean_store_order_field(self):
        invalid_dict = self.valid_order_schema.copy()
        invalid_data = fake_data.pylist(value_types=["int", "pyfloat", "str", "password"])
        invalid_dict['complete'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.order_endpoint)

    def test_invalid_type_integer_pet_field(self):
        invalid_dict = self.valid_pet_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "pyfloat", "str", "password"])
        invalid_dict['id'] = fake_data.random_element(invalid_data)
        invalid_dict['category']['id'] = fake_data.random_element(invalid_data)
        invalid_dict['tags'][0]['id'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.pet_endpoint)

    def test_invalid_type_integer_store_order_field(self):
        invalid_dict = self.valid_order_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "pyfloat", "str", "password"])
        invalid_dict['id'] = fake_data.random_element(invalid_data)
        invalid_dict['petId'] = fake_data.random_element(invalid_data)
        invalid_dict['quantity'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.order_endpoint)

    def test_invalid_type_integer_store_inventory_field(self):
        invalid_dict = self.valid_inventory_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "pyfloat", "str", "password"])
        for key in invalid_dict:
            invalid_dict[key] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.inventory_endpoint)

    def test_invalid_type_string_pet_field(self):
        invalid_dict = self.valid_pet_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "int", "pyfloat"])
        invalid_dict['category']['name'] = fake_data.random_element(invalid_data)
        invalid_dict['name'] = fake_data.random_element(invalid_data)
        invalid_dict['photoUrls'][0] = fake_data.random_element(invalid_data)
        invalid_dict['tags'][0]['name'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.pet_endpoint)

    def test_invalid_type_string_store_order_field(self):
        invalid_dict = self.valid_order_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "int", "pyfloat"])
        invalid_dict['shipDate'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.order_endpoint)

    def test_invalid_type_list_pet_field(self):
        invalid_dict = self.valid_pet_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "int", "pyfloat", "str", "password"])
        invalid_dict['photoUrls'] = fake_data.random_element(invalid_data)
        invalid_dict['tags'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.pet_endpoint)

    def test_invalid_type_dict_pet_field(self):
        invalid_dict = self.valid_pet_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "int", "pyfloat", "str", "password"])
        invalid_dict['category'] = fake_data.random_element(invalid_data)
        invalid_dict['tags'][0] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.pet_endpoint)

    def test_invalid_value_enum_pet_field(self):
        invalid_dict = self.valid_pet_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "int", "pyfloat", "str", "password"])
        invalid_dict['status'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.pet_endpoint)

    def test_invalid_value_enum_store_order_field(self):
        invalid_dict = self.valid_order_schema.copy()
        invalid_data = fake_data.pylist(value_types=["boolean", "int", "pyfloat", "str", "password"])
        invalid_dict['status'] = fake_data.random_element(invalid_data)
        with raises(AssertionError):
            assert_response_schema(invalid_dict, endpoint=self.order_endpoint)


def get_incomplete_dict(dict_to_cut):
    incomplete_dict = dict_to_cut.copy()
    random_keys = fake_data.random_elements(incomplete_dict.keys(), unique=True)
    for key in random_keys:
        incomplete_dict.pop(key)
    return incomplete_dict
