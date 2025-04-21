from pymongo import MongoClient
from config import Config

# MongoDB client and database setup
client = MongoClient(Config.MONGO_URI)
db = client["sports_feed_stg"]  # Your database name
venues_collection = db["cf_venues"]  # MongoDB collection

# Function to fetch venue data by fuzzy match
def get_venue_by_name(venue_name):
    venues = venues_collection.find({})
    venue_names = [venue['vde']['gdn'] for venue in venues]
    
    return venue_names
