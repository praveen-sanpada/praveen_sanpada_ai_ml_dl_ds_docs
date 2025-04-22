# === generate_script.py ===
from transformers import pipeline

with open("text_input.txt") as f:
    text = f.read()

summarizer = pipeline("summarization")
segments = summarizer(text, max_length=40, min_length=20, do_sample=False)

with open("script_segments.txt", "w") as f:
    for i, seg in enumerate(segments):
        f.write(f"Scene {i+1}: {seg['summary_text']}\n")

print("✅ Script segments saved to script_segments.txt")
