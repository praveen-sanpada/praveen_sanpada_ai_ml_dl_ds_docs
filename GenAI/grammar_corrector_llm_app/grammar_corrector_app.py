# 📁 Folder Structure: grammar_corrector_llm_app

# grammar_corrector_llm_app/
# └── grammar_corrector_app.py

# === grammar_corrector_app.py ===
import streamlit as st
import os
from transformers import pipeline
from spellchecker import SpellChecker
import difflib

# Set Streamlit page config first
st.set_page_config(page_title="Grammar + Spell Corrector", page_icon="✍️")

# Set compatibility env for protobuf
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# Load grammar correction model
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="vennify/t5-base-grammar-correction",
        tokenizer="vennify/t5-base-grammar-correction",
        max_length=512,
        do_sample=False
    )

# Load spell checker
@st.cache_resource
def load_spellchecker():
    return SpellChecker()

model = load_model()
spell = load_spellchecker()

# Custom whitelist to protect known names/entities
custom_dictionary = {
    "india": "india", "ind": "india", "pakistan": "pakistan", "pak": "pakistan",
    "t20": "t20", "odi": "odi", "score": "score", "match": "match"
}

# Try to fuzzy match to custom dictionary if spell correction fails
def correct_word(word):
    word_lower = word.lower()
    if word_lower in custom_dictionary:
        return custom_dictionary[word_lower]
    elif spell.unknown([word]):
        best_match = difflib.get_close_matches(word_lower, custom_dictionary.keys(), n=1)
        return custom_dictionary[best_match[0]] if best_match else word
    return word

# Spell correct each word with fallback
def spell_correct(text):
    words = text.split()
    corrected = [correct_word(w) for w in words]
    return " ".join(corrected)

# Streamlit UI
st.title("🧠 AI Text Corrector (Grammar + Spell Check)")
st.markdown("Fix grammar AND cricket-specific spelling using HuggingFace + fuzzy matching.")

text_input = st.text_area("Enter your sentence:", height=200)

if st.button("✅ Correct Text") and text_input.strip():
    with st.spinner("Correcting spelling..."):
        spell_fixed = spell_correct(text_input.strip())

    with st.spinner("Correcting grammar..."):
        output = model(f"grammar: {spell_fixed}")[0]["generated_text"]

    st.markdown("---")
    st.markdown("### 🔤 Spelling Fixed:")
    st.write(spell_fixed)

    st.markdown("### ✅ Grammar Corrected:")
    st.write(output.strip())