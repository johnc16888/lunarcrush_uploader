# drive_uploader.py

import os
import json
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_drive(filepath):
    # 从环境变量中加载 credentials JSON
    raw_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not raw_json:
        raise Exception("环境变量 GOOGLE_SERVICE_ACCOUNT_JSON 未设置")

    credentials_dict = json.loads(raw_json)
    credentials = service_account.Credentials.from_service_account_info(
        credentials_dict, scopes=["https://www.googleapis.com/auth/drive"]
    )

    service = build("drive", "v3", credentials=credentials)

    # 获取本月文件夹名称
    now = datetime.datetime.now()
    folder_name = f"{now.year}-{now.month:02d}"

    # 查询是否已有该文件夹
    folder_id = None
    query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    results = service.files().list(q=query, spaces="drive", fields="files(id, name)").execute()
    folders = results.get("files", [])

    if folders:
        folder_id = folders[0]["id"]
    else:
        # 创建新文件夹
        file_metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder"
        }
        folder = service.files().create(body=file_metadata, fields="id").execute()
        folder_id = folder.get("id")

    # 上传文件
    file_metadata = {
        "name": os.path.basename(filepath),
        "parents": [folder_id]
    }
    media = MediaFileUpload(filepath, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    file_id = uploaded_file.get("id")

    # 返回分享链接
    return f"https://drive.google.com/file/d/{file_id}/view"
