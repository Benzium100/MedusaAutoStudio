from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip
import os

audio_clip = AudioFileClip("story_audio.mp3")
duration_per_scene = audio_clip.duration / 5  # 5 scenes

clips = []
for i in range(1, 6):
    img_clip = ImageClip(f"images/scene_{i}.png").set_duration(duration_per_scene).fadein(1).fadeout(1)
    clips.append(img_clip)

video = concatenate_videoclips(clips, method="compose")

# Optional: background music
if os.path.exists("background_music.mp3"):
    bg_music = AudioFileClip("background_music.mp3").volumex(0.3)
    final_audio = CompositeVideoClip([audio_clip, bg_music])
    video.audio = final_audio.audio
else:
    video.audio = audio_clip

video.write_videofile("daily_video.mp4", fps=24, codec="libx264", audio_codec="aac")
print("Video created successfully.")
