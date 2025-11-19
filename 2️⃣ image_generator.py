import json
import requests
from PIL import Image
from io import BytesIO
import os
import sys

HF_API_KEY = os.getenv("HF_API_KEY")

with open("daily_story.json") as f:
    story = json.load(f)

os.makedirs("images", exist_ok=True)

for idx, scene in enumerate(story["scenes"], start=1):
    prompt = f"Cinematic, realistic, fantasy scene: {scene['description']}"
    response = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
        headers={"Authorization": f"Bearer {HF_API_KEY}"},
        json={"inputs": prompt},
    )
    image_bytes = response.content
    img = Image.open(BytesIO(image_bytes))
    img.save(f"images/scene_{idx}.png")
    print(f"Scene {idx} image saved.")
