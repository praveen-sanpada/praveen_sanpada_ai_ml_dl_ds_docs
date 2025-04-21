import streamlit as st
from chatbot_engine import LocalLLMChatBot

st.set_page_config(page_title="Offline LLM Chatbot", page_icon="🧠")
st.title("🧠 Local LLM ChatBot (Offline)")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = LocalLLMChatBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_query = st.chat_input("Ask me anything...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        reply = st.session_state.chatbot.get_response(user_query)
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
