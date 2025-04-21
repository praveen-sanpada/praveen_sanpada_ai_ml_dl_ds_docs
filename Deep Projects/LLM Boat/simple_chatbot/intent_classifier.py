# ===========================
# intent_classifier.py
# ===========================
def classify_query(query):
    q = query.lower()

    if any(word in q for word in ["hi", "hello", "hey"]):
        return "greeting"
    if "how are you" in q:
        return "check_wellbeing"
    if "your name" in q:
        return "ask_bot_name"
    if "what can you do" in q:
        return "ask_capabilities"
    if "who created you" in q:
        return "ask_creator"
    if "joke" in q:
        return "joke_request"
    if "can you help" in q:
        return "help_request"
    if "thank" in q:
        return "gratitude"
    if any(word in q for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    if "time" in q:
        return "get_current_time"

    return "unknown"