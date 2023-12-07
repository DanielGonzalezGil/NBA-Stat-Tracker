from player import Player
from stats import Stats


class APIHandler:
    def get_player_data(player_name):
        player = Player(player_name)
        return player.fetch_data()

    def get_player_stats(player_id, season):
        stats = Stats(player_id, season)
        return stats.fetch_season_averages()
