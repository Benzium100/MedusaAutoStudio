from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from moviepy.audio.fx.all import audio_fadein, audio_fadeout
import os

def main():
    clips = []
    for i in range(1, 6):
        clip = ImageClip(f"scene_{i}.png").set_duration(6*60)  # 6 minutes per scene
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    audio = AudioFileClip("story_audio.mp3")
    audio = audio_fadein(audio, 2).fx(audio_fadeout, 2)
    video = video.set_audio(audio)
    
    video.write_videofile("daily_video.mp4", fps=24, codec="libx264")
    print("Video generated!")

if __name__ == "__main__":
    main()
