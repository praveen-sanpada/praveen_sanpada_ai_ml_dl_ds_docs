# === app.py ===
import streamlit as st
from grammar_corrector import correct_grammar
import os

# Set compatibility env for protobuf
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

st.set_page_config(page_title="Grammar Corrector with LLM")
st.title("✍️ Grammar Corrector - Powered by LangChain")

user_input = st.text_area("Enter text to correct:", height=200)

if st.button("Correct Grammar") and user_input:
    corrected = correct_grammar(user_input)
    st.markdown("---")
    st.subheader("✅ Corrected Text:")
    st.write(corrected)