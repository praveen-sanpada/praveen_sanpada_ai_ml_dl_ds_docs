# === grammar_corrector.py ===
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from model_loader import load_llm
from prompts import grammar_prompt

llm = load_llm()
prompt = PromptTemplate.from_template(grammar_prompt)

chain = prompt | llm

def correct_grammar(text: str) -> str:
    return chain.invoke({"text": text}).strip()