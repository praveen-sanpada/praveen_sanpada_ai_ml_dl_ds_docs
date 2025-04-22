# === generate_images.py ===
from diffusers import StableDiffusionPipeline
import torch
import os

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

with open("script_segments.txt") as f:
    lines = f.readlines()

os.makedirs("assets", exist_ok=True)

for i, line in enumerate(lines):
    if line.strip():
        prompt = line.split(":", 1)[-1].strip()
        image = pipe(prompt).images[0]
        image.save(f"assets/scene_{i+1}.jpg")

print("✅ Images generated in assets/")