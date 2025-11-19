import json
from gtts import gTTS

with open("daily_story.json") as f:
    story = json.load(f)

text = " ".join([scene["text"] for scene in story["scenes"]])
tts = gTTS(text=text, lang="en")
tts.save("story_audio.mp3")

print("TTS audio generated: story_audio.mp3")
