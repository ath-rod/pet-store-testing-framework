import requests

from helpers.pet_wrapper import PetWrapper
from assertpy import assert_that

wrapper = PetWrapper()


def test_post_pet():
    pet_id, response = wrapper.create_pet()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.as_dict["id"]).is_equal_to(pet_id)

