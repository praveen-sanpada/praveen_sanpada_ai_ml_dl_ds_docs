import json
import pandas as pd

# Function to load the venue data from a JSON file
def load_venue_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to preprocess venue data and prepare it for the chatbot
def preprocess_data(data):
    venue_info = []

    for venue in data:
        venue_name = venue.get("vde", {}).get("gdn", "")
        venue_data = venue.get("odi", {}).get("sts", {})
        if venue_name and venue_data:
            venue_info.append({
                "venue_name": venue_name,
                "data": venue_data
            })
    return venue_info
