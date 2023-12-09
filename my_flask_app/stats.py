# Importing the requests library to make HTTP request
import requests


class Stats:
    BASE_URL = "https://www.balldontlie.io/api/v1/season_averages"

    # Constructor for the Stats class, initializes with player_id and season
    def __init__(self, player_id, season):
        self.player_id = player_id
        self.season = season

    # Method to fetch season averages for the specified player and season
    def fetch_season_averages(self):
        # Making a GET request to the API with player_id and season as parameters
        response = requests.get(
            f"{self.BASE_URL}",
            params={"player_ids[]": self.player_id, "season": self.season},
        )

        if response.status_code != 200:
            return None

        # Extracting and returning the data from the response
        data = response.json().get("data", [])
        if not data:
            return None

        simplified_data = data[0]
        return simplified_data
