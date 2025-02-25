from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# External API URL (Example: JSONPlaceholder for user data)
THIRD_PARTY_API = "https://jsonplaceholder.typicode.com/users"

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Radar Clone"})

@app.route("/external-data/<int:user_id>", methods=["GET"])
def get_external_data(user_id):
    """Fetches user data from a third-party API."""
    response = requests.get(f"{THIRD_PARTY_API}/{user_id}")
    
    if response.status_code != 200:
        return jsonify({"error": "Error fetching data"}), response.status_code

    return jsonify(response.json())

@app.route("/reverse-string", methods=["POST"])
def fetch_embeddings():
    """Query to OpenAi"""
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Please provide a 'query' field in JSON"}), 400
    text = data["query"]
    #Open AI call
    reversed_text = text[::-1]
    
    return jsonify({"original": text, "reversed": reversed_text})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
