import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fallbacks if .env fails
MONGO_URI = os.getenv("MONGO_URI") or "mongodb://ec2-35-154-176-120.ap-south-1.compute.amazonaws.com:27017"
DB_NAME = os.getenv("MONGO_DB") or "sports_feed_stg"
COLLECTION_NAME = os.getenv("MONGO_COLLECTION") or "cf_venues"

# Log the loaded values (optional for debug)
print("✅ MongoDB Config:")
print("URI:", MONGO_URI)
print("DB:", DB_NAME)
print("COLLECTION:", COLLECTION_NAME)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Fetch venue by partial/stadium name
# def fetch_venue_by_name(name):
#     return collection.find_one({"vde.gdn": {"$regex": name, "$options": "i"}})
def fetch_venue_by_name(name):
    return collection.find_one({
        "$or": [
            {"vde.gdn": {"$regex": name, "$options": "i"}},  # ground name
            {"vde.vnc": {"$regex": name, "$options": "i"}}   # venue city
        ]
    })

# Extract summary of last ODI match
def get_last_odi_match_summary(venue_data):
    odi_data = venue_data.get("odi", {})
    all_matches = odi_data.get("mch", {})
    if not all_matches:
        return "No ODI matches found at this venue."

    last_match = max(all_matches.items(), key=lambda x: x[1]["sdt"])[1]
    return (
        f"{last_match['tle']} was played on {last_match['sdt']} — "
        f"Final Score: {last_match['h']} {last_match['hts']}/{last_match['hwts']} "
        f"vs {last_match['a']} {last_match['ats']}/{last_match['awts']}."
    )
