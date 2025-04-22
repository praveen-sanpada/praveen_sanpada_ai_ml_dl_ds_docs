# ===========================
# mongo_utils.py
# ===========================
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Fetch values or fallback to defaults
MONGO_URI = os.getenv("MONGO_URI") or "mongodb://ec2-35-154-176-120.ap-south-1.compute.amazonaws.com:27017"
DB_NAME = os.getenv("MONGO_DB") or "sports_feed_stg"
COLLECTION_NAME = os.getenv("MONGO_COLLECTION") or "cf_venues"

# Debugging - Remove in production
print("✅ Mongo ENV:")
print("MONGO_URI =", MONGO_URI)
print("MONGO_DB =", DB_NAME)
print("MONGO_COLLECTION =", COLLECTION_NAME)

# Setup MongoDB
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def fetch_venue_by_name(name):
    return collection.find_one({
        "$or": [
            {"vde.gdn": {"$regex": name, "$options": "i"}},
            {"vde.vnc": {"$regex": name, "$options": "i"}}
        ]
    })