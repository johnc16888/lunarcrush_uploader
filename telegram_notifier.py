# telegram_notifier.py

import os
import requests

def send_telegram_alert(coins: list, excel_path: str):
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ 缺少 Telegram 环境变量")
        return

    if not coins:
        text = "⚠️ 本轮无符合条件的代币，未触发推送。"
    else:
        lines = ["📊 符合条件的代币（部分字段）：\n"]
        for i, coin in enumerate(coins, start=1):
            lines.append(f"{i}. {coin['symbol']} - {coin['name']}")
            lines.append(f"   AltRank: #{coin.get('altrank')}, Engagement: {coin.get('engagement')} ({coin.get('engagement_change')})")
            lines.append(f"   Mentions: {coin.get('mentions')} ({coin.get('mentions_change')}), 24h价格变化: {coin.get('price_change')}")
        text = "\n".join(lines)

    # 发送文本消息
    resp = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": text}
    )
    print(f"[INFO] 推送状态: {resp.status_code}")

    # 上传 Excel 文件（如果有）
    if excel_path and os.path.exists(excel_path):
        with open(excel_path, "rb") as f:
            resp = requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument",
                data={"chat_id": TELEGRAM_CHAT_ID},
                files={"document": f}
            )
            print(f"[INFO] Excel 文件上传状态: {resp.status_code}")
