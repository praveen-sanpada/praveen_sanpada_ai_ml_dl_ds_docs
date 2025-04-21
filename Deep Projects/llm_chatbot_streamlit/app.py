# ===========================
# app.py
# ===========================
import streamlit as st
from dotenv import load_dotenv
from chatbot_engine import MongoChatBot

load_dotenv()

st.set_page_config(page_title="🏏 Cricket Venue Bot", page_icon="🏟️")
st.title("🏏 Ask Anything About Cricket Venues")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = MongoChatBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your question (e.g., last ODI in Chennai)?")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    reply = st.session_state.chatbot.answer_query(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)