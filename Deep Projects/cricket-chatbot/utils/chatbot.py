from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf
import numpy as np
import json
from fuzzywuzzy import process

# Load pre-trained BERT model for text classification (or fine-tuned for your use case)
model = TFAutoModelForSequenceClassification.from_pretrained('bert-base-uncased')
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="tf", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.logits

def get_best_match(query, data):
    # Get the best venue match using fuzzy matching
    best_match = process.extractOne(query, [entry['venue_name'] for entry in data])
    return best_match[0] if best_match[1] > 80 else None

def get_venue_info(venue_name, data):
    for venue in data:
        if venue['venue_name'].lower() == venue_name.lower():
            return venue['data']
    return None

def chat_response(query, data):
    # Step 1: Use fuzzy matching to identify venue
    venue_name = get_best_match(query, data)
    if venue_name:
        venue_data = get_venue_info(venue_name, data)
        
        if venue_data:
            # Retrieve some relevant data for response (you can customize this)
            stats = venue_data.get("1", {}).get("o", {})
            return f"Venue: {venue_name}, RPO: {stats.get('rpo', 'N/A')}, Highest Score: {stats.get('hs', 'N/A')}"
        else:
            return f"Sorry, I couldn't find detailed information for {venue_name}."
    else:
        return "Sorry, I couldn't match any venue name with your query. Please check the spelling."
