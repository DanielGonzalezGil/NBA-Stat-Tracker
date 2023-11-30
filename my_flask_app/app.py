from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Balldontlie API base URL
BALL_DONT_LIE_API_BASE = "https://www.balldontlie.io/api/v1/"


# Simulated API endpoint
@app.route("/api/data", methods=["GET"])
def get_api_data():
    # Get the player name from the request parameters
    player_name = request.args.get("player_name")

    if not player_name:
        return jsonify({"error": "Player name is required"}), 400

    # API endpoint for player search
    player_search_endpoint = f"{BALL_DONT_LIE_API_BASE}players"
    params = {"search": player_name}

    # API call
    response = requests.get(player_search_endpoint, params=params)
    print(response.text)

    if response.status_code == 200:
        # Extract relevant player data
        player_data = response.json().get("data", [])

        return jsonify(player_data)
    else:
        return jsonify({"error": "Error fetching player data"}), response.status_code


# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
