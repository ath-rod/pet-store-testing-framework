from assertpy import soft_assertions, assert_that


def assert_body_is_the_same(expected, actual):  # TODO: consider nested dicts and add unit test
    with soft_assertions():
        for attribute in expected:
            assert_that(expected[attribute]).described_as(f"{attribute}").is_equal_to(actual[attribute])
