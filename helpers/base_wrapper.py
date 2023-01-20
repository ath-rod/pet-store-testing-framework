from config import BASE_URI


class BaseWrapper:
    def __init__(self, url_path=''):
        self.base_url = f"{BASE_URI}/{url_path}"
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
