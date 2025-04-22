import json
from datetime import datetime

with open("config/knowledge_base.json") as f:
    knowledge_base = json.load(f)

def generate_response(intent, query):
    static = {
        "get_current_time": f"🕒 The current time is {datetime.now().strftime('%H:%M:%S')}",
        "unknown": "🤔 I'm not sure how to answer that yet. Can you rephrase or ask another way?"
    }
    return knowledge_base.get(intent, static.get(intent, static["unknown"]))
