import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

API_KEY = os.getenv("YOUTUBE_API_KEY")
VIDEO_FILE = "daily_video.mp4"
THUMBNAIL_FILE = "thumbnail.png"

youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Medusa Cinematic Daily Story",
            "description": "Watch the cinematic Medusa story daily! #Fantasy #Action #Cinematic",
            "tags": ["Medusa", "Cinematic", "Fantasy", "DailyStory", "YouTubeAuto"],
            "categoryId": "24"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body=MediaFileUpload(VIDEO_FILE)
)
response = request.execute()

# Set thumbnail
youtube.thumbnails().set(
    videoId=response["id"],
    media_body=MediaFileUpload(THUMBNAIL_FILE)
).execute()

print(f"Video uploaded successfully: {response['id']}")
