import json
from json import JSONDecodeError
from json import loads

from base_wrapper import BaseWrapper
from config import BASE_URI
from core.api_core import APIRequest
from utils.get_data_set import get_pet


class PetWrapper(BaseWrapper):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI + 'pet'
        self.request = APIRequest()

    def create_pet(self, body=None):
        if body is None:
            pet_id, payload = get_pet()
        response = self.request.post(self.base_url, payload, self.headers)
        try:
            payload = json.loads(payload)
        except JSONDecodeError:
            payload = {}
        return pet_id, response, payload

    def get_pet_by_id(self, pet_id):
        url = f'{self.base_url}/{pet_id}'
        return self.request.get(url)

    def delete_pet_by_id(self, pet_id):
        url = f'{self.base_url}/{pet_id}'
        return self.request.delete(url)
