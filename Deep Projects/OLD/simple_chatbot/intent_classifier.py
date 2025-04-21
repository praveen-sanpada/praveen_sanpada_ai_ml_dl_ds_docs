# ===========================
# intent_classifier.py
# ===========================
from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

intent_map = {
    "greeting": ["hi", "hello", "hey there"],
    "check_wellbeing": ["how are you", "how's it going"],
    "ask_bot_name": ["what's your name", "who are you"],
    "ask_capabilities": ["what can you do", "how can you help me"],
    "ask_creator": ["who made you", "who created you"],
    "joke_request": ["tell me a joke", "make me laugh"],
    "help_request": ["can you help me", "i need assistance"],
    "gratitude": ["thank you", "thanks"],
    "goodbye": ["bye", "see you later", "goodbye"],
    "get_current_time": ["what time is it", "tell me the time"]
}

def classify_intent(query):
    query_vec = model.encode(query, convert_to_tensor=True)
    best_intent = "unknown"
    best_score = 0.5

    for intent, phrases in intent_map.items():
        phrase_vecs = model.encode(phrases, convert_to_tensor=True)
        cosine_scores = util.pytorch_cos_sim(query_vec, phrase_vecs)
        score = torch.max(cosine_scores).item()
        if score > best_score:
            best_intent = intent
            best_score = score

    return best_intent