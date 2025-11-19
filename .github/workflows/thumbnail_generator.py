from PIL import Image, ImageDraw, ImageFont
import json

with open("daily_story.json") as f:
    story = json.load(f)

# Base image from first scene
img = Image.open("images/scene_1.png").convert("RGB")
draw = ImageDraw.Draw(img)

# Add title text
font = ImageFont.load_default()
title = story["title"]
draw.text((50, 50), title, fill="yellow", font=font)

img.save("thumbnail.png")
print("Thumbnail generated successfully.")
