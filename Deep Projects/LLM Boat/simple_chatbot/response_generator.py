# ===========================
# response_generator.py
# ===========================
from datetime import datetime

def get_response(intent):
    responses = {
        "greeting": "Hello there! 👋",
        "check_wellbeing": "I'm just a bunch of code, but I'm doing great! How about you?",
        "ask_bot_name": "I'm your friendly chatbot assistant!",
        "ask_capabilities": "I can answer simple questions and chat with you!",
        "ask_creator": "I was created by an awesome developer. 😉",
        "joke_request": "Why don’t scientists trust atoms? Because they make up everything!",
        "help_request": "Of course! I'm here to help. Just ask your question!",
        "gratitude": "You're welcome! 😊",
        "goodbye": "Goodbye! Have a great day! 👋",
        "get_current_time": f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    }
    return responses.get(intent, "I'm not sure how to respond to that. Can you rephrase?")