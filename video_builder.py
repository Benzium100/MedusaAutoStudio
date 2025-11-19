import subprocess
import os

# Settings
image_folder = "./images"
audio_file = "story_audio.mp3"
output_video = "daily_video.mp4"
frame_duration = 10  # seconds per image (adjust for ~30-min video if many images)

# Create input.txt for FFmpeg
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])
with open("input.txt", "w") as f:
    for img in image_files:
        f.write(f"file '{os.path.join(image_folder, img)}'\n")
        f.write(f"duration {frame_duration}\n")
    f.write(f"file '{os.path.join(image_folder, image_files[-1])}'\n")  # repeat last frame

# FFmpeg command
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
print(f"Video created successfully: {output_video}"
