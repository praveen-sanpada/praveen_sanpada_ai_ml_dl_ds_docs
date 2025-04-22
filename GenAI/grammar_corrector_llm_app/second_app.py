# 📁 Folder Structure: grammar_corrector_llm_app

# grammar_corrector_llm_app/
# └── grammar_corrector_app.py

# === grammar_corrector_app.py ===
import streamlit as st
import os
from transformers import pipeline
from spellchecker import SpellChecker
import difflib
import re

# Set Streamlit page config first
st.set_page_config(page_title="Universal Grammar Corrector", page_icon="✍️")

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

# Enhanced fallback with global spell correction + fuzzy matching

def correct_word(word):
    word_clean = re.sub(r"[^a-zA-Z0-9]", "", word)  # remove special chars for spell check
    if word_clean.lower() in spell:
        return word
    elif spell.unknown([word_clean]):
        correction = spell.correction(word_clean)
        return correction if correction else word
    return word

# Spell correct each word in the sentence

def spell_correct(text):
    words = text.split()
    corrected = [correct_word(w) for w in words]
    return " ".join(corrected)

# Streamlit UI
st.title("🌐 Universal AI Grammar Corrector")
st.markdown("Fix **any text** with grammar and spelling correction using a HuggingFace model + spell checker.")

text_input = st.text_area("✏️ Enter any sentence:", height=200)

if st.button("🔧 Fix Grammar") and text_input.strip():
    with st.spinner("🛠 Fixing spelling..."):
        spell_fixed = spell_correct(text_input.strip())

    with st.spinner("✍️ Fixing grammar..."):
        output = model(f"grammar: {spell_fixed}")[0]["generated_text"]

    st.markdown("---")
    st.markdown("### 🧾 Spelling Fixed:")
    st.code(spell_fixed)

    st.markdown("### ✅ Grammar Corrected:")
    st.success(output.strip())