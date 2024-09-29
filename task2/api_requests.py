import requests
import config


class ApiRequest:
    def __init__(self):
        self.url = config.url

    def get_response(self):
        payload = config.payload
        headers = config.headers
        response = requests.request("GET", self.url, headers=headers, data=payload)
        return response.json()
