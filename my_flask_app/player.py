import requests


class Player:
    BASE_URL = "https://www.balldontlie.io/api/v1/"

    def __init__(self, name):
        self.name = name

    def fetch_data(self):
        response = requests.get(f"{self.BASE_URL}players", params={"search": self.name})
        if response.status_code != 200:
            return None
        return response.json().get("data", [])
