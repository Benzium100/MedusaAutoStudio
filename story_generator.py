import json

# 30-scene daily story about Princess Medusa
story = {
    "title": "Medusa the Princess",
    "scenes": [
        {"text": f"Scene {i+1}: Medusa faces a new challenge in her kingdom."} 
        for i in range(30)
    ]
}

with open("daily_story.json", "w") as f:
    json.dump(story, f, indent=4)

print("daily_story.json for Medusa created successfully!")
