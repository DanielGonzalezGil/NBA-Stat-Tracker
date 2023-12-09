# Importing the requests library to make HTTP requests
import requests


class Player:
    BASE_URL = "https://www.balldontlie.io/api/v1/"

    # Constructor for the Player class, initializes with player's name
    def __init__(self, name):
        self.name = name

    # Method to fetch data for the player with the given name
    def fetch_data(self):
        # Making a GET request to the API searching for the player by name
        response = requests.get(
            f"{self.BASE_URL}players",
            params={"search": self.name},
        )
        # Check if the response status code is 200 (OK), return None otherwise
        if response.status_code != 200:
            return None
        # Return the player data as JSON
        return response.json().get("data", [])
