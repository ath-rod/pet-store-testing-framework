import pytest

from core.api_core import APIRequest
from assertpy import assert_that

request = APIRequest()


@pytest.mark.apicore
def test_non_existing_pet():
    response = request.get('http://petstore.swagger.io/v2/pet/0')
    assert_that(response.status_code).is_equal_to(404)


@pytest.mark.apicore
def test_existing_pet():
    response = request.get('http://petstore.swagger.io/v2/pet/1000')
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.apicore
def test_connection_error():
    response = request.get('http://petstre.swagger.io/v2/pet/1234')
    assert_that(response.text).is_equal_to('ConnectionError')
