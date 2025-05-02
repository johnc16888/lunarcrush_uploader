# telegram_notifier.py

import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(coins, excel_path=None):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Telegram 配置未设置")
        return

    if not coins:
        message = "📭 本轮没有符合条件的代币"
    else:
        message = f"📈 本轮筛选出 {len(coins)} 个代币：\n\n"
        for i, coin in enumerate(coins, 1):
            message += (
                f"{i}. ${coin['symbol']} - {coin['name']}\n"
                f"📊 AltRank: {coin.get('altrank', 'N/A')} | Engagement: {coin.get('engagement_value', 'N/A')} ({coin.get('engagement_change', 'N/A')}%)\n"
                f"💬 Mentions: {coin.get('mention_value', 'N/A')} ({coin.get('mention_change', 'N/A')}%)\n"
                f"📈 Price Change: {coin.get('price_change', 'N/A')}%\n\n"
            )

    # 发送文本消息
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }
    response = requests.post(url, json=payload)
    print(f"[Telegram] 消息发送状态: {response.status_code}")

    # 如果指定了 Excel 文件路径，则上传
    if excel_path and os.path.exists(excel_path):
        with open(excel_path, "rb") as file:
            files = {"document": file}
            data = {"chat_id": TELEGRAM_CHAT_ID}
            file_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
            r = requests.post(file_url, data=data, files=files)
            print(f"[Telegram] Excel 文件发送状态: {r.status_code}")
