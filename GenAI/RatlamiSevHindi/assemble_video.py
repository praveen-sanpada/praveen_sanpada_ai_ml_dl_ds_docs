# === assemble_video.py ===
from moviepy.editor import *
import os

clips = []

# Total duration target (in seconds)
max_duration = 60
image_duration = 5  # seconds per image
num_required = min(max_duration // image_duration, 10)

for i in range(1, num_required + 1):
    img_path = f"assets/scene_{i}.jpg"
    audio_path = f"assets/voice_{i}.wav"
    if os.path.exists(img_path) and os.path.exists(audio_path):
        img_clip = ImageClip(img_path).set_duration(image_duration)
        audio_clip = AudioFileClip(audio_path)
        img_clip = img_clip.set_audio(audio_clip)
        # Optional: Add text overlay in Hindi
        txt_clip = TextClip("Ratlami Sev - पारंपरिक स्वाद", fontsize=32, font='Devanagari Sangam MN', color='white')
        txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(image_duration)
        final_clip = CompositeVideoClip([img_clip, txt_clip])
        clips.append(final_clip)

final = concatenate_videoclips(clips, method="compose")
os.makedirs("output", exist_ok=True)
final.write_videofile("output/ratlami_reel.mp4", fps=24)

print("🎉 Hindi audio video created at output/ratlami_reel.mp4")