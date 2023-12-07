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

    friendly_data = {column_names_mapping.get(k, k): v for k, v in stats_data.items()}

    friendly_data.pop("season", None)
    friendly_data.pop("player_id", None)
    friendly_data.pop("min", None)

    chart_data = {
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
    return jsonify(chart_data)


if __name__ == "__main__":
    app.run(debug=True)
