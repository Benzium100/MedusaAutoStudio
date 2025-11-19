import json
from gtts import gTTS
import os

with open("daily_story.json") as f:
    story = json.load(f)

text = " ".join([scene["description"] for scene in story["scenes"]])
tts = gTTS(text=text, lang="en", slow=False)
tts.save("story_audio.mp3")
print("Audio generated successfully.")
