from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Simulated API endpoint
@app.route("/api/data", methods=["GET"])
def get_api_data():
    # Replace this with actual API call or data retrieval logic
    data = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]
    return jsonify(data)


# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
