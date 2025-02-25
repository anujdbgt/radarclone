from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# External API URL (Example: JSONPlaceholder for user data)
THIRD_PARTY_API = "https://jsonplaceholder.typicode.com/users"

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Flask with 3rd Party API Call!"})

@app.route("/external-data/<int:user_id>", methods=["GET"])
def get_external_data(user_id):
    """Fetches user data from a third-party API."""
    response = requests.get(f"{THIRD_PARTY_API}/{user_id}")
    
    if response.status_code != 200:
        return jsonify({"error": "Error fetching data"}), response.status_code

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
