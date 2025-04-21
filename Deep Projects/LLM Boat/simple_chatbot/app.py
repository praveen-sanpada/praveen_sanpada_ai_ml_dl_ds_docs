# ===========================
# app.py
# ===========================
import streamlit as st
from intent_classifier import classify_query
from response_generator import get_response

st.set_page_config(page_title="🤖 Simple Chatbot")
st.title("💬 Daily Conversation Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Say something like 'Hi' or 'Tell me a joke'...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    intent = classify_query(user_input)
    reply = get_response(intent)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
