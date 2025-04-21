from mongo_utils import fetch_venue_by_name, get_last_odi_match_summary

class MongoChatBot:
    def __init__(self):
        pass  # You can add LLM model loading here if needed

    def answer_query(self, query):
        query = query.lower()

        # Example 1: Last ODI match at venue
        if "last odi" in query:
            venue_name = self.extract_venue_name(query)
            venue_data = fetch_venue_by_name(venue_name)
            if venue_data:
                return get_last_odi_match_summary(venue_data)
            else:
                return f"Sorry, I couldn't find any venue matching '{venue_name}'."

        return "I couldn't understand your query. Try asking about venue statistics."

    def extract_venue_name(self, query):
        # Simple venue name extractor
        for possible in ["dharamsala", "chennai", "mumbai", "kolkata"]:
            if possible.lower() in query:
                return possible
        return "Himachal Pradesh Cricket Association Stadium"
