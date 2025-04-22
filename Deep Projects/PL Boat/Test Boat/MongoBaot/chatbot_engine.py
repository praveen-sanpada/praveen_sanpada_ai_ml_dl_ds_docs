# ===========================
# chatbot_engine.py
# ===========================
from mongo_utils import fetch_venue_by_name
from intent_classifier import classify_query
from query_router import query_router

class MongoChatBot:
    def answer_query(self, query):
        venue_name = self.extract_venue_name(query)
        venue_data = fetch_venue_by_name(venue_name)

        if not venue_data:
            return f"❌ Venue '{venue_name}' not found."

        intent = classify_query(query)
        return query_router(intent, query, venue_data)

    def extract_venue_name(self, query):
        for v in ["chennai", "dharamsala", "mumbai", "kolkata"]:
            if v in query.lower():
                return v
        return "chennai"