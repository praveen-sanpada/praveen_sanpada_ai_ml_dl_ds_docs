import streamlit as st
from utils.data_loader import load_venue_data, preprocess_data
from utils.chatbot import chat_response

# Load venue data
venue_data = load_venue_data('data/venues.json')
preprocessed_data = preprocess_data(venue_data)

# Streamlit UI
st.title('Cricket Venue Chatbot')

# User input for venue-related questions
user_query = st.text_input("Ask me about a cricket venue (e.g., 'What is the RPO at Narendra Modi Stadium?')")

if user_query:
    response = chat_response(user_query, preprocessed_data)
    st.write(response)
