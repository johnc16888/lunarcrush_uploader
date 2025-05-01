import json
import os

credentials = os.getenv("GOOGLE_CREDENTIALS_JSON")
if not credentials:
    print("❌ 未检测到 GOOGLE_CREDENTIALS_JSON 环境变量")
    exit(1)

with open("credentials.json", "w") as f:
    f.write(credentials)
print("✅ 已成功写入 credentials.json")