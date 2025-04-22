# === model_loader.py ===
from transformers import pipeline
from langchain.llms import HuggingFacePipeline  # Updated import path
from langchain_community.llms import HuggingFacePipeline 
from functools import lru_cache

@lru_cache(maxsize=1)
def load_llm():
    pipe = pipeline(
        "text2text-generation",
        model="vennify/t5-base-grammar-correction",
        tokenizer="vennify/t5-base-grammar-correction",
        max_length=512,
        do_sample=False
    )
    return HuggingFacePipeline(pipeline=pipe)