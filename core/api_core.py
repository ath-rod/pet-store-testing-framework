from dataclasses import dataclass
from json import JSONDecodeError

import requests

from utils.custom_strings import error_name


@dataclass
class Response:
    status_code: int
    body_as_raw: str
    body_as_dict: object
    headers: dict


class APIRequest:
    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_response_data(response)

    def put(self, url, payload, headers):
        response = requests.put(url, data=payload, headers=headers)
        return self.__get_response_data(response)

    def get(self, url):
        response = requests.get(url)
        return self.__get_response_data(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_response_data(response)

    @staticmethod
    def __get_response_data(response):
        status_code = response.status_code
        body_as_raw = response.text
        headers = response.headers

        try:
            body_as_dict = response.json()
        except JSONDecodeError as error:
            if len(body_as_raw) > 200:
                body_as_raw = f"{body_as_raw[:150]} ... {body_as_raw[-40:]}"
            raise Exception(f"{error_name(error)} raised from status code {status_code}, headers: {headers},"
                            f"and body {body_as_raw}")

        return Response(
            status_code, body_as_raw, body_as_dict, headers
        )
