import json
from gtts import gTTS

with open("daily_story.json") as f:
    story = json.load(f)

full_text = " ".join(scene["description"] for scene in story["scenes"])
tts = gTTS(full_text, lang="en")
tts.save("story_audio.mp3")
