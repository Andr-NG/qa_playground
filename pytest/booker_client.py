# flake8: noqa

import requests



class Client:

    def __init__(self, url):
        self.url = url

    def create_token(self, creds: dict):
        URL = self.url + "/auth"
        token_req = requests.post(url=URL, json=creds)
        token_req.raise_for_status()
        return token_req.json()

    def create_booking(self, booking_data=dict):
        URL = self.url + "/booking"
        token_req = requests.post(url=URL, json=booking_data)
        token_req.raise_for_status()
        return token_req.json()


