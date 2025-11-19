import json
import requests
import os

HF_API_KEY = os.environ.get("HF_API_KEY")
with open("daily_story.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

os.makedirs("images", exist_ok=True)

for scene in scenes:
    filename = f"images/scene_{scene['scene_number']}.png"
    if os.path.exists(filename):
        print(f"Cached image found: {filename}")
        continue

    prompt = f"{scene['title']}: {scene['description']}, cinematic, realistic, high detail, fantasy, dramatic lighting"

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

    for attempt in range(3):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            img_bytes = response.content
            with open(filename, "wb") as f_img:
                f_img.write(img_bytes)
            print(f"Generated image: {filename}")
            break
        except Exception as e:
            print(f"Retry {attempt+1}/3 failed for {filename}: {e}")
