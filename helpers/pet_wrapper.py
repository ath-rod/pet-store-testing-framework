from dataclasses import dataclass
from json import dumps

from base_wrapper import BaseWrapper
from core.api_core import APIRequest
from utils.get_data_set import generate_pet


@dataclass
class Request:
    headers: dict
    payload: dict
    response: object
    pet_id: int


class PetWrapper(BaseWrapper):
    def __init__(self):
        super().__init__(url_path='pet')
        self.request = APIRequest()

    def post_pet(self, payload=None) -> object:
        if payload is None:
            payload = generate_pet()
        pet_id = payload['id']
        response = self.request.post(self.base_url, dumps(payload), self.headers)

        return Request(
            self.headers, payload, response, pet_id
        )

    def get_pet_by_id(self, pet_id) -> object:
        url = f'{self.base_url}/{pet_id}'
        return self.request.get(url)

    def delete_pet_by_id(self, pet_id) -> object:
        url = f'{self.base_url}/{pet_id}'
        return self.request.delete(url)

    def put_pet(self, payload: dict) -> object:
        return self.request.put(self.base_url, dumps(payload), self.headers)
