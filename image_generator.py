import json
import os
import requests

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# Load story
with open("daily_story.json") as f:
    story = json.load(f)

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

for i, scene in enumerate(story["scenes"]):
    prompt = f"Cinematic, highly detailed scene: {scene['title']} - {scene['description']}"
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        image_bytes = response.content
        image_path = f"images/scene_{i+1}.png"
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        print(f"Saved image: {image_path}")
    else:
        print(f"Failed to generate image for scene {i+1}: {response.text}")
