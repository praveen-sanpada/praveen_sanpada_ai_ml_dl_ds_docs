import logging
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=f"logs/chatbot_{datetime.now().strftime('%Y-%m-%d')}.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

def log_user_query(user_input, corrected_input, intent):
    logging.info(f"User: {user_input}")
    if user_input != corrected_input:
        logging.info(f"Corrected: {corrected_input}")
    logging.info(f"Intent detected: {intent}")

def log_response(reply):
    logging.info(f"Bot: {reply}")

def log_error(error_msg):
    logging.error(f"Error: {error_msg}")
