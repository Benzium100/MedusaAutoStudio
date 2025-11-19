# thumbnail_generator.py
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import os

# Config
thumbnail_path = "thumbnail.png"
width, height = 1280, 720  # YouTube recommended 1280x720
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # adjust if needed

# Example story title (can be loaded from your JSON story)
story_titles = [
    "Medusa's Dark Secret",
    "The Cursed Princess",
    "Battle of Shadows",
    "Medusa's Revenge",
    "The Hidden Labyrinth"
]
title_text = random.choice(story_titles)

# Create base thumbnail
bg_colors = ["#0B0C10", "#1F2833", "#4B4B4B", "#2C3E50"]
bg_color = random.choice(bg_colors)
thumbnail = Image.new("RGB", (width, height), color=bg_color)

draw = ImageDraw.Draw(thumbnail)

# Optional: add a vignette effect
for i in range(200):
    draw.rectangle(
        [i, i, width-i, height-i],
        outline=(0,0,0, int(255*(i/200)))
    )

# Add story title text
font_size = 70
font = ImageFont.truetype(font_path, font_size)
margin = 40
max_width = width - 2*margin
lines = textwrap.wrap(title_text, width=20)  # wrap text to fit thumbnail

y_text = height//2 - (len(lines) * font_size)//2
for line in lines:
    w, h = draw.textsize(line, font=font)
    draw.text(((width-w)/2, y_text), line, font=font, fill="white", stroke_width=2, stroke_fill="black")
    y_text += h + 10

# Optional: add a random cinematic accent (like glowing eyes or effect)
accent_color = random.choice(["#FF0000", "#00FFFF", "#FFD700"])
draw.ellipse([width-200, 50, width-100, 150], fill=accent_color)

# Save thumbnail
thumbnail.save(thumbnail_path)
print(f"Thumbnail saved to {thumbnail_path}")
