import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Fetch secrets from environment (GitHub Actions will inject these)
YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]
YOUTUBE_CLIENT_SECRET_FILE = os.environ["YOUTUBE_CLIENT_SECRET_FILE"]  # JSON for OAuth
YOUTUBE_REFRESH_TOKEN = os.environ["YOUTUBE_REFRESH_TOKEN"]

VIDEO_FILE = "daily_video.mp4"
THUMBNAIL_FILE = "thumbnail.png"

# Video details (You can customize your title & description pro tips)
VIDEO_TITLE = "Medusa: Daily Fantasy Adventure ⚔️🔥"
VIDEO_DESCRIPTION = (
    "Dive into today's cinematic Medusa story! "
    "Fantasy, action, suspense—all in one epic adventure. "
    "Subscribe and watch daily! 🔔"
)
VIDEO_TAGS = ["Medusa", "Fantasy", "Daily Story", "Action", "Cinematic", "AI Video"]

def upload_video():
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": VIDEO_TITLE,
                "description": VIDEO_DESCRIPTION,
                "tags": VIDEO_TAGS,
                "categoryId": "24"  # Entertainment
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=media
    )

    response = request.execute()
    print(f"Uploaded video with ID: {response['id']}")

    # Upload thumbnail
    youtube.thumbnails().set(
        videoId=response['id'],
        media_body=MediaFileUpload(THUMBNAIL_FILE)
    ).execute()
    print("Thumbnail uploaded!")

if __name__ == "__main__":
    upload_video()
