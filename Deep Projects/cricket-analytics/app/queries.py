from app.models import LangChainModel
from app.data_processing import fetch_venue_data
import re

# Create LangChain model instance
llm = LangChainModel()

# Intent handler function
def handle_user_query(query):
    query_lower = query.lower()
    
    # Sample intent-based logic
    if "average first innings" in query_lower:
        venue = extract_venue(query)
        return get_first_innings_avg(venue)
    
    if "average second innings" in query_lower:
        venue = extract_venue(query)
        return get_second_innings_avg(venue)
    
    if "chasing" in query_lower:
        venue = extract_venue(query)
        return get_chasing_advantage(venue)
    
    # If no intent matches, use LangChain LLM to generate response
    return llm.get_response(query)

# Helper function to extract venue from the query
def extract_venue(query):
    venues = ["MA Chidambaram Stadium", "Wankhede", "Eden Gardens", "M Chinnaswamy", "Chepauk"]
    for venue in venues:
        if venue.lower() in query.lower():
            return venue
    return None

# Fetch first innings average score
def get_first_innings_avg(venue):
    venue_data = fetch_venue_data(venue)
    if venue_data:
        avg_score = venue_data["first_innings_avg"]
        return f"At {venue}, the average first innings score is {avg_score}."
    return "Data not found for the specified venue."

# Fetch second innings average score
def get_second_innings_avg(venue):
    venue_data = fetch_venue_data(venue)
    if venue_data:
        avg_score = venue_data["second_innings_avg"]
        return f"At {venue}, the average second innings score is {avg_score}."
    return "Data not found for the specified venue."

# Get chasing advantage
def get_chasing_advantage(venue):
    venue_data = fetch_venue_data(venue)
    if venue_data:
        advantage = venue_data["chasing_advantage"]
        return f"Chasing at {venue} has a {advantage}% win rate."
    return "Data not found for the specified venue."
