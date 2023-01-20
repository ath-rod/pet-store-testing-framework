import json
from json import JSONDecodeError

from base_wrapper import BaseWrapper
from core.api_core import APIRequest
from utils.get_data_set import get_pet


class PetWrapper(BaseWrapper):
    def __init__(self):
        super().__init__(url_path='pet')
        self.request = APIRequest()

    def create_pet(self, body=None):
        if body is None:
            pet_id, payload = get_pet()
        response = self.request.post(self.base_url, payload, self.headers)
        # TODO: create an object for the info sent as request, remove this try catch as it will be unnecessary after
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
