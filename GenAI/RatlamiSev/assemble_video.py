# === assemble_video.py ===
from moviepy.editor import *
import os

clips = []
for i in range(1, 10):
    img_path = f"assets/scene_{i}.jpg"
    audio_path = f"assets/voice_{i}.wav"
    if os.path.exists(img_path) and os.path.exists(audio_path):
        img_clip = ImageClip(img_path).set_duration(5)
        audio_clip = AudioFileClip(audio_path)
        img_clip = img_clip.set_audio(audio_clip)
        clips.append(img_clip)

final = concatenate_videoclips(clips, method="compose")
os.makedirs("output", exist_ok=True)
final.write_videofile("output/ratlami_reel.mp4", fps=24)

print("🎉 Video created at output/ratlami_reel.mp4")