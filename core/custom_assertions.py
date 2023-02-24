from assertpy import soft_assertions, assert_that
from cerberus import Validator


def assert_dicts_are_equal(expected_dict, actual_dict, parent_path=""):
    with soft_assertions():
        if isinstance(expected_dict, dict) and isinstance(actual_dict, dict):
            for key, value in expected_dict.items():
                path = f"{parent_path}.{key}" if parent_path else key
                try:
                    assert_that(actual_dict, f"Actual dict doesn't contain {path}").contains_key(key)
                    if isinstance(value, list) and isinstance(actual_dict[key], list):
                        for expected_item, actual_item in zip(value, actual_dict[key]):
                            assert_dicts_are_equal(expected_item, actual_item, parent_path=f"{path}.{expected_item}")
                    else:
                        assert_dicts_are_equal(expected_dict[key], actual_dict[key], parent_path=path)
                except KeyError:
                    pass  # Handled in first assert
        else:
            assert_that(actual_dict, f"{parent_path}").is_equal_to(expected_dict)


def assert_response_schema(response, expected_schema, allow_unknown=False):
    """
    Asserts response follows the expected schema
    WARNING: doesn't work with soft assertions, if this fails, it will not show other failures in same test
    Args:
        response: dict to be compared
        expected_schema: dict with the expected rules to validate (cerberus syntax)
        allow_unknown: bool to raise assertion errors if there are more fields than specified in schema, default:False

    Returns: raises AssertionError with the list of schema errors found in response, nothing if it's valid.
    """
    schema_validator = Validator(require_all=True, allow_unknown=allow_unknown)
    if schema_validator.validate(response, expected_schema) is False:
        raise AssertionError(schema_validator.errors)
