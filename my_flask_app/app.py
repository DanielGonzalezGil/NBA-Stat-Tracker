from flask import Flask, render_template, request, jsonify
from api_handler import APIHandler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/data", methods=["GET"])
def get_api_data():
    player_name = request.args.get("player_name")
    if not player_name:
        return jsonify({"error": "Player name is required"}), 400
    player_data = APIHandler.get_player_data(player_name)
    if player_data is None:
        return jsonify({"error": "Error fetching player data"}), 500
    return jsonify(player_data)


@app.route("/api/player_stats/chart", methods=["GET"])
def player_stats_chart():
    player_id = request.args.get("player_id")
    season = request.args.get("season")
    stats_data = APIHandler.get_player_stats(player_id, season)
    if not stats_data:
        return jsonify({"error": "No stats data found"}), 404

    # Define a mapping of column names to user-friendly names
    column_names_mapping = {
        "games_played": "Games Played",
        "fgm": "Field Goals Made",
        "fga": "Field Goals Attempted",
        "fg3m": "Three-Point Field Goals Made",
        "ftm": "Free Throws Made",
        "oreb": "Offensive Rebounds",
        "reb": "Total Rebounds",
        "stl": "Steals",
        "turnover": "Turnovers",
        "pts": "Points",
        "ast": "Assists",
        "fg3_pct": "Three-Point Field Goal %"
        # Add more mappings as necessary
    }

    # Rename the keys using the mapping
    friendly_data = {column_names_mapping.get(k, k): v for k, v in stats_data.items()}

    # Exclude 'player_id' and 'season' if they are still present
    friendly_data.pop("season", None)
    friendly_data.pop("player_id", None)

    # # Exclude certain columns from the data
    # stats_data.pop("player_id", None)
    # stats_data.pop("season", None)

    # Format for Chart.js
    chart_data = {
        "labels": list(friendly_data.keys()),  # Convert to list
        "datasets": [
            {
                "label": f"Season {season} Averages",
                "data": list(friendly_data.values()),  # Convert to list
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1,
            }
        ],
    }
    return jsonify(chart_data)


if __name__ == "__main__":
    app.run(debug=True)
