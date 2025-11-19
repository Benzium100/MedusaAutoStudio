import json
import requests
import os

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
with open("daily_story.json") as f:
    story = json.load(f)

for idx, scene in enumerate(story["scenes"], start=1):
    prompt = f"{scene['description']} cinematic, highly detailed, realistic, 720p landscape"
    response = requests.post(
        "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"inputs": prompt}
    )
    image_bytes = response.content
    with open(f"scene_{idx}.png", "wb") as img_file:
        img_file.write(image_bytes)
