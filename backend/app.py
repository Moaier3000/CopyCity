from flask import Flask, request, jsonify
from flask_cors import CORS
from services.llm_service import get_recommendations

app = Flask("CopyCity_Server")
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    city = data.get("city")
    preferences = data.get("preferences")

    if not city:
        return jsonify({"error": "City is required"}), 400

    result = get_recommendations(city, preferences)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)