from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, current_app
from app.services.llm_service import get_recommendations

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("CopyCity_wizard_page_html.html")

@main.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    
    result = get_recommendations(data)
    
    session['recommendations'] = result
    
    return jsonify({"status": "success", "redirect": url_for("main.page2")})

@main.route("/map")
def page2():
    recommendations = session.get('recommendations', [])
    return render_template(
        "CopyCity_map_page_html.html", 
        google_maps_api_key=current_app.config["GOOGLE_MAPS_API_KEY"],
        recommendations=recommendations
    )