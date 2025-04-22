from transformers import pipeline

grammar_pipeline = pipeline("text2text-generation", model="prithivida/grammar_error_correcter_v1", device=-1)

def correct_grammar(text):
    return grammar_pipeline(text)[0]['generated_text']
