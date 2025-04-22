import json
import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("config/intents.json") as f:
    intent_map = json.load(f)

def classify_intent(query):
    query_vec = model.encode(query, convert_to_tensor=True)
    best_intent = "unknown"
    best_score = 0.5

    for intent, examples in intent_map.items():
        example_vecs = model.encode(examples, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(query_vec, example_vecs)
        max_score = torch.max(scores).item()
        if max_score > best_score:
            best_score = max_score
            best_intent = intent

    return best_intent
