# tts_generator.py
from gtts import gTTS
import json

# Load the daily story JSON
with open("daily_story.json", "r") as f:
    story = json.load(f)

# Combine all scene texts into one string
full_text = ""
for scene in story["scenes"]:
    full_text += f"{scene['title']}: {scene['description']}\n"

# Generate TTS audio
tts = gTTS(text=full_text, lang="en", slow=False)
tts.save("story_audio.mp3")

print("Text-to-speech audio generated successfully as story_audio.mp3")
