from dataclasses import dataclass

import requests

from utils.custom_strings import error_name


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:
    def get(self, url):
        try:
            response = requests.get(url)
            return self.__get_successful_response(response)

        except Exception as error:
            return self.__get_unsuccessful_response(error)

    def post(self, url, payload, headers):
        try:
            response = requests.post(url, data=payload, headers=headers)
            return self.__get_successful_response(response)

        except Exception as error:
            return self.__get_unsuccessful_response(error)

    def delete(self, url):
        try:
            response = requests.delete(url)
            return self.__get_successful_response(response)

        except Exception as error:
            return self.__get_unsuccessful_response(error)

    @staticmethod
    def __get_successful_response(response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )

    @staticmethod
    def __get_unsuccessful_response(error):
        status_code = 0
        text = error_name(error)
        as_dict = {'error type': error_name(error)}
        headers = {}

        return Response(
            status_code, text, as_dict, headers
        )
