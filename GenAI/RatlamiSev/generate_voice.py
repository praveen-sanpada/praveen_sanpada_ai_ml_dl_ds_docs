# === generate_voice.py ===
from gtts import gTTS
import os

with open("script_segments.txt") as f:
    lines = f.readlines()

os.makedirs("assets", exist_ok=True)

for i, line in enumerate(lines):
    if line.strip():
        scene_text = line.split(":", 1)[-1].strip()
        tts = gTTS(text=scene_text, lang='en')
        tts.save(f"assets/voice_{i+1}.wav")

print("✅ Voice files generated using gTTS in assets/")