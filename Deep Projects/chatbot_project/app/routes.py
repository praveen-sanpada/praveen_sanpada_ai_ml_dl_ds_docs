from flask import Blueprint, request, jsonify
from .nlp import process_query

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/ask', methods=['POST'])
def ask():
    query = request.json.get('query')
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    response = process_query(query)
    return jsonify({"response": response})
