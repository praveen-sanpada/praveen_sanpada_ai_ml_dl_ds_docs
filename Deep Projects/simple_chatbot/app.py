# ===========================
# app.py
# ===========================
import streamlit as st
from intent_classifier import classify_intent
from response_generator import generate_response
from model_loader import get_grammar_corrector

st.set_page_config(page_title="🤖 LLM Chatbot (No OpenAI)", page_icon="🧠")
st.title("🧠 Smart Chatbot Powered by Open-Source LLMs")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "grammar_model" not in st.session_state:
    st.session_state.grammar_model = get_grammar_corrector()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type a message (e.g. 'Hi', 'Tell me a joke')")
if user_input:
    corrected = st.session_state.grammar_model(user_input)[0]['generated_text']
    st.session_state.messages.append({"role": "user", "content": corrected})
    with st.chat_message("user"):
        st.markdown(corrected)

    intent = classify_intent(corrected)
    reply = generate_response(intent, corrected)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)