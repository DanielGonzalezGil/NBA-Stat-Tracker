import requests
import pandas as pd
import io
import matplotlib.pyplot as plt
import plotly.express as px


class Stats:
    BASE_URL = "https://www.balldontlie.io/api/v1/"

    def __init__(self, player_id, season):
        self.player_id = player_id
        self.season = season

    def fetch_season_averages(self):
        response = requests.get(
            f"{self.BASE_URL}season_averages",
            params={"player_ids[]": self.player_id, "season": self.season},
        )
        if response.status_code != 200:
            return None
        return response.json().get("data", [])

    def generate_stats_graph(self, stats_data):
        df = pd.DataFrame([stats_data])
        fig, ax = plt.subplots(figsize=(10, 6))
        df.plot(kind="bar", ax=ax)
        ax.set_title(f"Player Statistics for {self.season} Season")
        ax.set_ylabel("Statistics")
        ax.set_xlabel("Categories")

        img = io.BytesIO()
        plt.savefig(img, format="png", bbox_inches="tight")
        img.seek(0)
        return img
