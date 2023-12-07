import requests


class Stats:
    BASE_URL = "https://www.balldontlie.io/api/v1/season_averages"

    def __init__(self, player_id, season):
        self.player_id = player_id
        self.season = season

    def fetch_season_averages(self):
        response = requests.get(
            f"{self.BASE_URL}",
            params={"player_ids[]": self.player_id, "season": self.season},
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", [])
        if not data:
            return None

        simplified_data = data[0]
        return simplified_data
