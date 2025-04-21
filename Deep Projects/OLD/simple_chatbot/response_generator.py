# ===========================
# response_generator.py
# ===========================
from datetime import datetime

def generate_response(intent, query):
    responses = {
        "greeting": "Hello! 👋 How can I assist you today?",
        "check_wellbeing": "I'm running great on clean code! 😊 How are you doing?",
        "ask_bot_name": "I'm a chatbot powered by open-source LLMs and deep learning!",
        "ask_capabilities": "I can chat, correct grammar, and help with basic daily questions.",
        "ask_creator": "I was created by a developer using Hugging Face Transformers!",
        "joke_request": "Why don’t programmers like nature? Too many bugs! 🐛",
        "help_request": "Of course! Just ask me anything you need help with.",
        "gratitude": "You're welcome! 🤗",
        "goodbye": "Goodbye! Come back anytime! 👋",
        "get_current_time": f"The current time is {datetime.now().strftime('%H:%M:%S')} ⏰."
    }
    return responses.get(intent, "I'm not sure how to answer that yet. Can you try rephrasing?")