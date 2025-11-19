import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

YOUTUBE_API_KEY = os.getenv("YT_API_KEY")
VIDEO_FILE = "daily_video.mp4"
TITLE = "Medusa: Daily Epic"
DESCRIPTION = "Watch Medusa's cinematic adventure unfold daily! #Medusa #Fantasy #Cinematic"
THUMBNAIL_FILE = "thumbnail.png"

def main():
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": TITLE,
                "description": DESCRIPTION,
                "tags": ["Medusa", "Cinematic", "Fantasy"],
                "categoryId": "1"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(VIDEO_FILE)
    )
    response = request.execute()
    video_id = response['id']
    # Upload thumbnail
    youtube.thumbnails().set(videoId=video_id, media_body=THUMBNAIL_FILE).execute()
    print("Video uploaded!")

if __name__ == "__main__":
    main()
