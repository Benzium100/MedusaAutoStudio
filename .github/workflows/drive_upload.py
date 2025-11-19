from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import os

# Path to your service account JSON
SERVICE_JSON = os.getenv("DRIVE_CREDENTIALS")
FOLDER_ID = "1z31EvfCYWt1lSNCurqD4IPkk1DOHYBJG"  # Your Drive folder ID
VIDEO_FILE = "daily_video.mp4"

credentials = service_account.Credentials.from_service_account_file(SERVICE_JSON, scopes=["https://www.googleapis.com/auth/drive.file"])
drive_service = build('drive', 'v3', credentials=credentials)

file_metadata = {
    'name': VIDEO_FILE,
    'parents': [FOLDER_ID]
}

media = MediaFileUpload(VIDEO_FILE, mimetype='video/mp4')
file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print(f"Uploaded video with File ID: {file.get('id')}")
