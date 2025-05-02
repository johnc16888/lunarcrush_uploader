import os
import requests

def send_telegram_alert(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("❌ Telegram 凭证缺失，请检查环境变量。")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Telegram 推送成功")
        else:
            print(f"❌ Telegram 推送失败: {response.text}")
    except Exception as e:
        print(f"❌ Telegram 错误: {e}")
