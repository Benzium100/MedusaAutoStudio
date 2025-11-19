import json
import os
from PIL import Image, ImageDraw, ImageFont

# Load your daily story JSON
story_file = "daily_story.json"

if not os.path.exists(story_file):
    print("ERROR: daily_story.json not found!")
    exit(1)

with open(story_file, "r") as f:
    story = json.load(f)

# Create images folder
image_folder = "./images"
os.makedirs(image_folder, exist_ok=True)

# Generate one image per scene
for idx, scene in enumerate(story["scenes"], start=1):
    img = Image.new("RGB", (1920, 1080), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Simple text overlay (you can replace with AI-generated images later)
    font = ImageFont.load_default()
    draw.text((50, 50), scene["text"], fill="black", font=font)
    
    file_path = os.path.join(image_folder, f"scene_{idx}.png")
    img.save(file_path)
    print(f"Saved {file_path}")

print(f"All {len(story['scenes'])} images generated in {image_folder}")
