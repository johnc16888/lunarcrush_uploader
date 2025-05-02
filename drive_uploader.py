# drive_uploader.py

import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json

def upload_to_drive(excel_path):
    credentials_dict = json.loads(os.environ.get("GOOGLE_CREDENTIALS_JSON", "{}"))
    credentials = service_account.Credentials.from_service_account_info(
        credentials_dict, scopes=["https://www.googleapis.com/auth/drive"]
    )

    service = build("drive", "v3", credentials=credentials)

    # 检查是否存在目标文件夹 LunarCrush-Upload
    folder_name = "LunarCrush-Upload"
    folders = (
        service.files()
        .list(q=f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and trashed = false",
              spaces="drive",
              fields="files(id, name)")
        .execute()
        .get("files", [])
    )
    if folders:
        parent_folder_id = folders[0]["id"]
    else:
        file_metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
        }
        file = service.files().create(body=file_metadata, fields="id").execute()
        parent_folder_id = file.get("id")

    # 创建当月子文件夹（如 2025-05）
    month_folder_name = datetime.datetime.now().strftime("%Y-%m")
    subfolders = (
        service.files()
        .list(q=f"'{parent_folder_id}' in parents and name='{month_folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
              spaces="drive",
              fields="files(id)")
        .execute()
        .get("files", [])
    )

    if subfolders:
        month_folder_id = subfolders[0]["id"]
    else:
        file_metadata = {
            "name": month_folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_folder_id],
        }
        file = service.files().create(body=file_metadata, fields="id").execute()
        month_folder_id = file.get("id")

    # 上传文件
    file_name = os.path.basename(excel_path)
    media = MediaFileUpload(excel_path, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    file_metadata = {"name": file_name, "parents": [month_folder_id]}
    uploaded = service.files().create(body=file_metadata, media_body=media, fields="id, webViewLink").execute()

    print(f"[✅] 文件已上传至 Google Drive: {uploaded.get('webViewLink')}")
    return uploaded.get("webViewLink")
