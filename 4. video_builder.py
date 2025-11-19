from moviepy.editor import *
import os

# Load all images
image_files = sorted([f"images/{f}" for f in os.listdir("images") if f.endswith(".png")])

# Load story narration
audio_clip = AudioFileClip("story_audio.mp3")

# Load background music (optional, can be looped)
bg_music = AudioFileClip("background_music.mp3").volumex(0.2)  # reduce volume

# Make sure background music matches audio duration
if bg_music.duration < audio_clip.duration:
    bg_music = afx.audio_loop(bg_music, duration=audio_clip.duration)

# Combine narration and background music
final_audio = CompositeAudioClip([bg_music, audio_clip])

# Generate video clips with fade-in/out transitions
clips = []
num_images = len(image_files)
scene_duration = audio_clip.duration / num_images

for img_file in image_files:
    clip = ImageClip(img_file).set_duration(scene_duration)
    clip = clip.crossfadein(1).crossfadeout(1)  # 1-second fade transitions
    clips.append(clip)

# Concatenate all clips smoothly
video = concatenate_videoclips(clips, method="compose")
video = video.set_audio(final_audio)
video.write_videofile(
    "daily_video.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac",
    preset="ultrafast",
    threads=4
)

print("Cinematic video with transitions and background music generated!")
