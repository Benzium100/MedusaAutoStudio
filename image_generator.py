import json
from PIL import Image, ImageDraw, ImageFont
import os

with open("daily_story.json") as f:
    story = json.load(f)

os.makedirs("images", exist_ok=True)
font = ImageFont.load_default()

for i, scene in enumerate(story["scenes"]):
    img = Image.new("RGB", (1280, 720), color=(30, 30, 60))  # Dark cinematic background
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), scene["text"], fill="white", font=font)
    img_path = f"images/scene_{i+1}.png"
    img.save(img_path)

print(f"{len(story['scenes'])} cinematic images generated successfully!")
