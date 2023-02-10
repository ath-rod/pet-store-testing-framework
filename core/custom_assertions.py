from assertpy import soft_assertions, assert_that


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
