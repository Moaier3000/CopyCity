from flask import current_app
from flask import Blueprint, request, jsonify, render_template
from app.services.llm_service import get_recommendations

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("CopyCity_wizard_page_html.html")


@main.route("/map")
def page2():
    return render_template("CopyCity_map_page_html.html", google_maps_api_key=current_app.config["GOOGLE_MAPS_API_KEY"])

@main.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    city = data.get("city")
    preferences = data.get("preferences")

    if not city:
        return jsonify({"error": "City is required"}), 400

    result = get_recommendations(city, preferences)

    return jsonify(result)