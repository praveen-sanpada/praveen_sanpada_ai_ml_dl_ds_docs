from pymongo import MongoClient
from config.settings import MONGO_URI, DB_NAME, COLLECTION_NAME

# Connect to MongoDB
def get_db_connection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

# Fetch data for a given venue
def fetch_venue_data(venue):
    collection = get_db_connection()
    data = collection.find_one({"venue_name": venue})
    
    if data:
        # Example of extracting venue-specific data
        return {
            "first_innings_avg": data["first_innings"]["average"],
            "second_innings_avg": data["second_innings"]["average"],
            "chasing_advantage": data["chasing_win_rate"]
        }
    return None
