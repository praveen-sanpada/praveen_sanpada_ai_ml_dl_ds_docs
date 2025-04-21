from flask import Blueprint, request, jsonify
from models.venue_model import get_venue_by_name
from utils.fuzzy_matcher import get_best_match

bp = Blueprint('venue', __name__)

@bp.route('/get-venue', methods=['POST'])
def get_venue():
    try:
        data = request.get_json()
        venue_name = data.get("venue_name")

        if not venue_name:
            return jsonify({"error": "Venue name is required"}), 400

        # Get the best match using fuzzy matching
        venue_names = get_venue_by_name(venue_name)
        best_match = get_best_match(venue_name, venue_names)

        if best_match:
            return jsonify({"matched_venue": best_match}), 200
        else:
            return jsonify({"error": "No matching venue found"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
