import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

API_KEY = os.getenv("YT_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Medusa Daily Adventure",
            "description": "A cinematic fantasy action story about Medusa. Subscribe for daily episodes!",
            "tags": ["Medusa","Fantasy","Cinematic","DailyStory","Action"],
            "categoryId": "24"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body=MediaFileUpload("daily_video.mp4")
)
response = request.execute()
print(response)
