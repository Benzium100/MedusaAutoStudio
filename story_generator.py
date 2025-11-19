import json
import random

# 30-minute cinematic Medusa story broken into 5 long scenes
scenes = [
    {"title": "Medusa Awakens", "description": "Medusa rises in her secret palace, shadows flickering, snakes hissing. The wind carries secrets of her destiny."},
    {"title": "The Forbidden Forest", "description": "Medusa travels through the enchanted forest. Monsters lurk, mystical lights guide her path, suspense thick in the air."},
    {"title": "The Ancient Temple", "description": "She enters the ancient temple, booby traps and mystical glyphs surround her. Every step is tense, action building."},
    {"title": "Battle with Shadows", "description": "Dark forces attack. Medusa wields her powers, intense battle choreography, cinematic slow-motion moments."},
    {"title": "Triumphant Escape", "description": "Medusa escapes, victorious yet hunted. The climax concludes in a breathtaking sunset, setting up tomorrow's story."}
]

random.shuffle(scenes)

with open("daily_story.json", "w") as f:
    json.dump({"scenes": scenes}, f, indent=4)
