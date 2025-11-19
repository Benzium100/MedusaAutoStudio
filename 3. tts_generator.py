import json
from gtts import gTTS
import os

def main():
    with open("daily_story.json") as f:
        story = json.load(f)
    text = ""
    for scene in story["scenes"]:
        text += f"{scene['title']}. {scene['description']}\n"
    tts = gTTS(text, lang="en")
    tts.save("story_audio.mp3")
    print("TTS audio generated!")

if __name__ == "__main__":
    main()
