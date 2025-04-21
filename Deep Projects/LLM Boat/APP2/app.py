import streamlit as st
from dotenv import load_dotenv
from chatbot_engine import MongoChatBot

# Load environment
load_dotenv()

st.set_page_config(page_title="🏏 Venue LLM ChatBot", page_icon="🤖")
st.title("🏏 Chat with Cricket Venue Bot")

# Initialize chatbot
if "chatbot" not in st.session_state:
    st.session_state.chatbot = MongoChatBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask me about venue stats, last ODI match...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from chatbot
    reply = st.session_state.chatbot.answer_query(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
