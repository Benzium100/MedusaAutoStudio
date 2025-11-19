import os
from huggingface_hub import InferenceClient

# Get Hugging Face API key from GitHub secret
hf_api_key = os.getenv("HF_API_KEY")

client = InferenceClient(hf_api_key)

# Example usage
prompt = "Cinematic Medusa fantasy scene, realistic style"
result = client.text_to_image(prompt)
with open("scene_1.png", "wb") as f:
    f.write(result)
