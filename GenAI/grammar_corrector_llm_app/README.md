# === README.md ===
# Grammar Correction LLM App

This project uses a T5-based Hugging Face model with LangChain and Streamlit to create a web app for grammar correction.

## 🔧 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧠 Model Used
- Model: `vennify/t5-base-grammar-correction` (Hugging Face)

## 🛠 Environment Setup Notes
- Uses HuggingFace Transformers + LangChain core
- Requires `protobuf==3.20.3` for compatibility with both TF and transformers
- Compatible with Python 3.8 to 3.10

---
Ready to correct grammar and polish text in real-time using cutting-edge LLMs!