from random import shuffle

from faker import Faker
from pytest import raises

from core.custom_assertions import assert_dicts_are_equal, assert_response_schema
from resources.random_data_generator import fake_data
from utils.get_data_set import generate_pet

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

    def test_valid_pet_schema(self):
        assert_response_schema(self.valid_pet_schema, endpoint="pet")
