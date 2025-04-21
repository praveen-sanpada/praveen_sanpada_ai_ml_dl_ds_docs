import streamlit as st
from intent_classifier import classify_intent
from response_generator import generate_response
from grammar_corrector import correct_grammar
from logger import log_user_query, log_response, log_error

st.set_page_config(page_title="🤖 Advanced LLM Chatbot", page_icon="🧠")
st.title("🧠 Chat with AI - Daily + Domain Expert Questions")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask anything like 'What's the average first innings score?' or 'Tell me a joke'")
if user_input:
    try:
        corrected_input = correct_grammar(user_input)
        intent = classify_intent(corrected_input)
        reply = generate_response(intent, corrected_input)

        log_user_query(user_input, corrected_input, intent)
        log_response(reply)

        st.session_state.messages.append({"role": "user", "content": corrected_input})
        with st.chat_message("user"):
            st.markdown(corrected_input)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        log_error(str(e))
        st.error("An error occurred while processing your request.")
