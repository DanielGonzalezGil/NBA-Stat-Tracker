from player import Player  # Importing the Player class to handle player data
from stats import Stats  # Importing the Stats class to handle player statistics


# Class for handling API requests related to basketball player information and statistics
class APIHandler:
    # Static method to get data for a specific player by name
    def get_player_data(player_name):
        player = Player(player_name)
        return player.fetch_data()

    # Static method to get season averages for a specific player by ID and season
    def get_player_stats(player_id, season):
        # Creating an instance of Stats with the given player ID and seaso
        stats = Stats(player_id, season)

        return stats.fetch_season_averages()
