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
        return pet_id, response
