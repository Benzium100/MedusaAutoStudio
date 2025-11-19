from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os

audio = AudioFileClip("story_audio.mp3")
clips = []

for i in range(1, 6):
    img_clip = ImageClip(f"scene_{i}.png").set_duration(audio.duration / 5).fadein(1).fadeout(1)
    clips.append(img_clip)

final_video = concatenate_videoclips(clips)
final_video = final_video.set_audio(audio)
final_video.write_videofile("daily_video.mp4", fps=24, codec="libx264")
