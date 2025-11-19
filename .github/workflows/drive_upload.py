import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Secrets stored in GitHub Actions
GOOGLE_CLIENT_SECRETS_FILE = os.environ["GOOGLE_CLIENT_SECRETS_FILE"]
VIDEO_FILE = "daily_video.mp4"

def upload_to_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(GOOGLE_CLIENT_SECRETS_FILE)
    gauth.LocalWebserverAuth()  # GitHub Actions will handle token flow

    drive = GoogleDrive(gauth)

    file_drive = drive.CreateFile({'title': os.path.basename(VIDEO_FILE)})
    file_drive.SetContentFile(VIDEO_FILE)
    file_drive.Upload()
    print(f"Video uploaded to Google Drive: {VIDEO_FILE}")

if __name__ == "__main__":
    upload_to_drive()
