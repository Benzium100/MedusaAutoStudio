import json
import random

# Long cinematic Medusa story, broken into dynamic scenes
scenes = [
    {"title": "Medusa Awakens", "description": "Medusa opens her eyes in the dark temple..."},
    {"title": "The Cursed Forest", "description": "She ventures through the mystical forest, hearing whispers..."},
    {"title": "Battle of Shadows", "description": "Monsters attack, but Medusa fights with her powers..."},
    {"title": "Allies Revealed", "description": "A mysterious figure helps her navigate the dangers..."},
    {"title": "The Final Confrontation", "description": "Medusa faces the dark lord in an epic showdown..."}
]

# Duplicate or shuffle scenes to reach 30-min video length (~10x)
final_scenes = []
for i in range(10):
    for scene in scenes:
        s = scene.copy()
        s["scene_number"] = len(final_scenes)+1
        final_scenes.append(s)

# Save to JSON
with open("daily_story.json", "w", encoding="utf-8") as f:
    json.dump(final_scenes, f, ensure_ascii=False, indent=4)

print("Story JSON generated with", len(final_scenes), "scenes.")
