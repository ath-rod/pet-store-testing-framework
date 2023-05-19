from dataclasses import dataclass
from json import dumps
from pprint import pformat

from config import logger
from core.api_core import APIRequest
from helpers.base_wrapper import BaseWrapper
from utils.get_data_set import generate_order


@dataclass
class Request:
    headers: dict
    payload: dict
    response: object


class StoreWrapper(BaseWrapper):
    def __init__(self):
        super().__init__(url_path='store')
        self.request = APIRequest()

    def post_order(self, pet_id=None, payload=None) -> object:
        url = f'{self.base_url}/order'
        if payload is None:
            payload = generate_order(pet_id)

        response = self.request.post(url, dumps(payload), self.headers)
        logger.info(f"POST ORDER: {pformat(response)}")

        return Request(
            self.headers, payload, response
        )

    def get_order_by_id(self, order_id) -> object:
        url = f'{self.base_url}/order/{order_id}'
        response = self.request.get(url)
        logger.info(f"GET ORDER: {pformat(response)}")
        return response

    def delete_order_by_id(self, order_id) -> object:
        url = f'{self.base_url}/order/{order_id}'
        response = self.request.delete(url)
        logger.info(f"DELETE ORDER: {pformat(response)}")
        return response

    def put_order(self, payload: dict) -> object:
        url = f'{self.base_url}/order'
        response = self.request.put(url, dumps(payload), self.headers)
        logger.info(f"PUT ORDER: {pformat(response)}")
        return response

    def get_store_inventory(self) -> object:
        url = f'{self.base_url}/inventory'
        response = self.request.get(url)
        logger.info(f"GET INVENTORY: {pformat(response)}")
        return response
