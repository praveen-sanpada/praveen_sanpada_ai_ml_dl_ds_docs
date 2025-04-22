# ===========================
# model_loader.py
# ===========================
from transformers import pipeline

def get_grammar_corrector():
    return pipeline("text2text-generation", model="prithivida/grammar_error_correcter_v1", device=-1)