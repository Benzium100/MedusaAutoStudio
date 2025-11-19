from gtts import gTTS
import json

with open("daily_story.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

full_text = " ".join([s["description"] for s in scenes])
tts = gTTS(full_text, lang="en")
tts.save("story_audio.mp3")
print("TTS audio generated.")
