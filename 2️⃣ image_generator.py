from huggingface_hub import InferenceClient

# Insert your API key here
API_KEY = "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"

client = InferenceClient(token=API_KEY)

prompt = "A cinematic fantasy scene of Medusa as a princess in action, suspenseful, cinematic lighting"
result = client.text_to_image(prompt)

# Save the image
with open("scene_1.png", "wb") as f:
    f.write(result)
