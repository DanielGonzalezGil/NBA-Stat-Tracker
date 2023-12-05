from flask import Flask, render_template, request, jsonify, send_file
from api_handler import APIHandler

app = Flask(__name__)


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


@app.route("/api/player_stats/graph", methods=["GET"])
def get_player_stats_graph():
    player_id = request.args.get("player_id")
    season = request.args.get("season")
    img = APIHandler.get_player_stats_graph(player_id, season)
    if img is None:
        return jsonify({"error": "Error generating player stats graph"}), 500
    return send_file(img, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
