import json
import random

def generate_story():
    scenes = [
        {"title": "The Awakening", "description": "Medusa wakes in a hidden palace surrounded by snakes, sensing danger."},
        {"title": "The Forbidden Forest", "description": "She ventures through a dark, mystical forest, encountering magical creatures."},
        {"title": "The Battle", "description": "Medusa faces rival warriors in a suspenseful and cinematic action scene."},
        {"title": "The Betrayal", "description": "An ally turns against her, intensifying the drama and tension."},
        {"title": "The Triumph", "description": "She overcomes her enemies and finds inner strength, ending the story in victory."}
    ]
    random.shuffle(scenes)
    story = {"title": "Medusa: Daily Epic", "scenes": scenes}
    with open("daily_story.json", "w") as f:
        json.dump(story, f, indent=4)
    print("Story generated!")

if __name__ == "__main__":
    generate_story()
