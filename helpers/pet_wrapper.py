from dataclasses import dataclass
from json import dumps
from pprint import pprint

from base_wrapper import BaseWrapper
from core.api_core import APIRequest
from utils.get_data_set import generate_pet


@dataclass
class Request:
    headers: dict
    payload: dict
    response: object


class PetWrapper(BaseWrapper):
    def __init__(self):
        super().__init__(url_path='pet')
        self.request = APIRequest()

    def post_pet(self, payload=None) -> object:
        if payload is None:
            payload = generate_pet()
        response = self.request.post(self.base_url, dumps(payload), self.headers)
        print("\n!!!POST PET:")
        pprint(response)
        return Request(self.headers, payload, response)

    def get_pet_by_id(self, pet_id) -> object:
        url = f'{self.base_url}/{pet_id}'
        response = self.request.get(url)
        print("\n!!!GET PET:")
        pprint(response)
        return response

    def delete_pet_by_id(self, pet_id) -> object:
        url = f'{self.base_url}/{pet_id}'
        response = self.request.delete(url)
        print("\n!!!DELETE PET:")
        pprint(response)
        return response

    def put_pet(self, payload: dict) -> object:
        response = self.request.put(self.base_url, dumps(payload), self.headers)
        print("\n!!!PUT PET:")
        pprint(response)
        return response
