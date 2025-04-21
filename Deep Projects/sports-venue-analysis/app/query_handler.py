import pymongo

# MongoDB Connection Setup
client = pymongo.MongoClient("mongodb://ec2-35-154-176-120.ap-south-1.compute.amazonaws.com:27017")
db = client["sports_feed_stg"]
collection = db["cf_venues"]

def fetch_venue_data(venue_name):
    """
    Fetch venue data from MongoDB by the venue name.
    """
    venue_data = collection.find_one({"vde.gdn": venue_name})
    if venue_data:
        return venue_data
    else:
        return None

def process_query(query, venue_data):
    """
    Process a query and return the relevant information based on the venue data.
    For simplicity, this function returns static data in response.
    You can customize this to include more detailed query processing based on your data structure.
    """
    # Example response: If the user asks for the average score, return the value
    if "average score" in query.lower():
        return f"The average score for matches at {venue_data['vde']['gdn']} is {venue_data['odi']['sts']['1']['o']['as']}."
    
    return "Sorry, I couldn't understand the query. Please try again."

def answer_user_query(query, venue_name):
    """
    Answer user query by fetching venue data and processing it.
    """
    venue_data = fetch_venue_data(venue_name)
    
    if venue_data:
        return process_query(query, venue_data)
    else:
        return f"Venue '{venue_name}' not found in the database."
