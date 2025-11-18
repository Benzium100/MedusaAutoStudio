# video_builder.py
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
import json
import os

# Configuration
IMAGE_FOLDER = "./images"  # folder where scene images are saved
AUDIO_FILE = "story_audio.mp3"  # TTS audio
BACKGROUND_MUSIC = "background_music.mp3"  # optional, lower volume if used
OUTPUT_FILE = "daily_video.mp4"
IMAGE_DURATION = 5  # seconds per image if no audio segmentation

# Load story JSON
with open("daily_story.json", "r") as f:
    story = json.load(f)

# Build image clips
clips = []
for idx, scene in enumerate(story["scenes"], start=1):
    image_path = os.path.join(IMAGE_FOLDER, f"scene_{idx}.png")
    if os.path.exists(image_path):
        clip = ImageClip(image_path).set_duration(IMAGE_DURATION)
        clips.append(clip)
    else:
        print(f"Warning: {image_path} not found. Skipping.")

if not clips:
    raise ValueError("No image clips found. Make sure your images are generated correctly.")

video = concatenate_videoclips(clips, method="compose")

# Add TTS audio
if os.path.exists(AUDIO_FILE):
    narration = AudioFileClip(AUDIO_FILE)
    video = video.set_audio(narration)
else:
    print("Warning: TTS audio not found. Video will be silent.")

# Optionally add background music
if os.path.exists(BACKGROUND_MUSIC):
    bg_music = AudioFileClip(BACKGROUND_MUSIC).volumex(0.2)
    if video.audio:
        video = video.set_audio(CompositeAudioClip([video.audio, bg_music]))
    else:
        video = video.set_audio(bg_music)

# Export final video
video.write_videofile(
    OUTPUT_FILE,
    fps=24,
    codec="libx264",
    audio_codec="aac",
    preset="medium",
    threads=4,
)

print(f"Video successfully created: {OUTPUT_FILE}")
