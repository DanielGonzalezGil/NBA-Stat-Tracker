# Importing necessary modules and classes
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)  # Flask for web app, render_template for HTML template, request for handling requests, jsonify for JSON responses
from api_handler import (
    APIHandler,
)  # Importing API handler for processing API calls
from flask_cors import CORS  # Importing CORS to handle cross-origin requests

# Initializing the Flask application
app = Flask(__name__)
CORS(app)  # Enabling CORS for all routes in the app


# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")


# Route for handling API requests for player data
@app.route("/api/data", methods=["GET"])
def get_api_data():
    # Retrieving the player name from the request arguments
    player_name = request.args.get("player_name")

    # Checking if the player name is provided, return an error if not
    if not player_name:
        return jsonify({"error": "Player name is required"}), 400
    player_data = APIHandler.get_player_data(player_name)
    if player_data is None:
        return jsonify({"error": "Error fetching player data"}), 500
    return jsonify(player_data)


# Route for handling API requests for player statistics chart
@app.route("/api/player_stats/chart", methods=["GET"])
def player_stats_chart():
    # Retrieving player ID and season from the request arguments
    player_id = request.args.get("player_id")
    season = request.args.get("season")

    # Fetching player statistics using the APIHandler
    stats_data = APIHandler.get_player_stats(player_id, season)
    # Handling the case where stats data is not found
    if not stats_data:
        return jsonify({"error": "No stats data found"}), 404

    # Mapping column names to more friendly names for the chart
    column_names_mapping = {
        "games_played": "Games Played",
        "fgm": "Field Goals Made",
        "fga": "Field Goals Attempted",
        "fg3m": "Three-Point Field Goals Made",
        "fg3a": "Three-Point Field Goals Attempted",
        "ftm": "Free Throws Made",
        "fta": "Free Throws Attempted",
        "oreb": "Offensive Rebounds",
        "dreb": "Defensive Rebounds",
        "reb": "Total Rebounds",
        "stl": "Steals",
        "blk": "Blocks",
        "turnover": "Turnovers",
        "pf": "Personal Fouls",
        "pts": "Points",
        "fg_pct": "Field Goal %",
        "ast": "Assists",
        "fg3_pct": "Three-Point Field Goal %",
        "ft_pct": "Free Throw %",
    }

    # Going through mapping column to replace abbreviations
    friendly_data = {column_names_mapping.get(k, k): v for k, v in stats_data.items()}

    # Removing unnecessary fields from the data
    friendly_data.pop("season", None)
    friendly_data.pop("player_id", None)
    friendly_data.pop("min", None)

    # Preparing the data for the chart
    chart_data = {
        # Formatting the data for the chart
        "labels": list(friendly_data.keys()),
        "datasets": [
            {
                "label": f"Season {season} Averages",
                "data": list(friendly_data.values()),
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1,
            }
        ],
    }

    # Return the chart data as JSON
    return jsonify(chart_data)


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
