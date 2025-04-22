# === generate_voice.py ===
from gtts import gTTS
import os
from googletrans import Translator

translator = Translator()
with open("script_segments.txt") as f:
    lines = f.readlines()

os.makedirs("assets", exist_ok=True)

for i, line in enumerate(lines):
    if line.strip():
        scene_text = line.split(":", 1)[-1].strip()
        translated = translator.translate(scene_text, dest='hi').text
        tts = gTTS(text=translated, lang='hi')
        tts.save(f"assets/voice_{i+1}.wav")

print("✅ Hindi voice files generated in assets/")