import subprocess
import os

# Settings
image_folder = "./images"  # Folder containing scene_1.png, scene_2.png, etc.
audio_file = "story_audio.mp3"
output_video = "daily_video.mp4"
frame_duration = 5  # seconds per image

# Generate input.txt for FFmpeg
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])
with open("input.txt", "w") as f:
    for img in image_files:
        f.write(f"file '{os.path.join(image_folder, img)}'\n")
        f.write(f"duration {frame_duration}\n")
    # Repeat last image to match audio length
    f.write(f"file '{os.path.join(image_folder, image_files[-1])}'\n")

# Build the video using FFmpeg
cmd = [
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", "input.txt",
    "-i", audio_file,
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest",
    output_video
]

subprocess.run(cmd, check=True)

print(f"Video created successfully: {output_video}")
