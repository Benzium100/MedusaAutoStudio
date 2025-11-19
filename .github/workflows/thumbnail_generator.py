# thumbnail_generator.py
import os
from huggingface_hub import InferenceClient
from PIL import Image, ImageDraw, ImageFont

# ---------- SETTINGS ----------
HF_API_KEY = os.getenv("HF_API_KEY")  # Your Hugging Face API key stored in GitHub Secrets
OUTPUT_FILE = "thumbnail.png"
TITLE_TEXT = "Medusa: Daily Adventure"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Change if needed
FONT_SIZE = 60
IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720
MODEL = "runwayml/stable-diffusion-v1-5"  # Stable Diffusion model

# ---------- GENERATE BASE IMAGE ----------
client = InferenceClient(HF_API_KEY)
prompt = (
    "Cinematic fantasy scene, Medusa as a heroic princess in action, "
    "dramatic lighting, mystical environment, 4k cinematic composition"
)

result = client.text_to_image(prompt, model=MODEL)
img = Image.open(result)
img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))

# ---------- ADD TITLE TEXT ----------
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

# Center text
text_width, text_height = draw.textsize(TITLE_TEXT, font=font)
x = (IMAGE_WIDTH - text_width) // 2
y = IMAGE_HEIGHT - text_height - 50  # Slightly above bottom
# Add outline for readability
outline_range = 3
for ox in range(-outline_range, outline_range+1):
    for oy in range(-outline_range, outline_range+1):
        draw.text((x+ox, y+oy), TITLE_TEXT, font=font, fill="black")
draw.text((x, y), TITLE_TEXT, font=font, fill="white")

# ---------- SAVE THUMBNAIL ----------
img.save(OUTPUT_FILE)
print(f"Thumbnail saved as {OUTPUT_FILE}")
