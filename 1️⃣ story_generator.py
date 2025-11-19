import json
import random
from datetime import datetime

def generate_story():
    # 30-min cinematic story, broken into scenes
    scenes = [
        {"title": "The Royal Chambers", "description": "Medusa awakens in her palace as shadows creep in..."},
        {"title": "The Forbidden Garden", "description": "She walks through the enchanted garden, every step revealing hidden secrets."},
        {"title": "The Battle Begins", "description": "Dark forces approach, and Medusa draws her legendary weapons."},
        {"title": "Chase Through the Caves", "description": "Twisting, echoing caves become a battlefield of magic and steel."},
        {"title": "Triumph and Revelation", "description": "Medusa confronts the final enemy, discovering her true power and destiny."},
    ]

    random.shuffle(scenes)
    story = {"title": f"Medusa Daily Tale {datetime.now().strftime('%Y-%m-%d')}", "scenes": scenes}

    with open("daily_story.json", "w") as f:
        json.dump(story, f, indent=4)
    print("Story generated successfully.")

if __name__ == "__main__":
    generate_story()
