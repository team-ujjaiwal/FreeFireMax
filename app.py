from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://aditya-items-v3op.onrender.com/items"
VALID_KEY = "14sectionskeysforujjaiwal"

@app.route("/items", methods=["GET"])
def custom_items():
    # Get all query parameters from the request
    params = request.args.to_dict()

    # Check for missing or invalid key
    user_key = params.get("key")
    if not user_key or user_key != VALID_KEY:
        return jsonify({"error": "Missing or invalid API key 🔑"}), 401

    try:
        # Forward the query (including the valid key) to the original API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": "Failed to fetch items", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)