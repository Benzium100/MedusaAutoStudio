import json
import requests
from PIL import Image
from io import BytesIO
import os

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL = "runwayml/stable-diffusion-v1-5"

def generate_image(prompt, index):
    url = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(url, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        img_data = response.content
        with open(f"scene_{index+1}.png", "wb") as f:
            f.write(img_data)
        print(f"Image for scene {index+1} saved.")
    else:
        print("Error generating image:", response.text)

def main():
    with open("daily_story.json") as f:
        story = json.load(f)
    for idx, scene in enumerate(story["scenes"]):
        generate_image(scene["description"], idx)

if __name__ == "__main__":
    main()
