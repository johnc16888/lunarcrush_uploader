# telegram_notifier.py

import os
import requests

def notify_results(filtered_data, drive_url=None):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("[ERROR] Telegram 环境变量未设置")
        return

    if filtered_data:
        message = "📈 本轮符合条件的代币:\n\n"
        for coin in filtered_data:
            message += f"🔹 {coin['Name']} (${coin['Symbol']})\n"
            message += f"📉 价格: {coin['Price']}\n"
            message += f"📊 Altrank: {coin['Altrank']}\n"
            message += f"💬 Engagement: {coin['Engagement']} ({coin['Engagement_Change']})\n"
            message += f"💡 Mentions: {coin['Mentions']} ({coin['Mentions_Change']})\n"
            message += f"💱 价格变化: {coin['Price_Change']}\n"
            message += "\n"
    else:
        message = "❌ 本轮没有符合条件的代币。\n"

    if drive_url:
        message += f"📊 本轮筛选结果已上传至 Google Drive：\n🔗 下载链接: {drive_url}"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("[INFO] 已成功发送 Telegram 通知")
    else:
        print(f"[ERROR] Telegram 推送失败: {response.text}")
