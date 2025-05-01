import os
import requests

def send_telegram_summary(tokens, drive_url):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not tokens:
        msg = f"📊 本轮未发现符合条件的代币\n🎯 AltRank ≤ 50 且 Engagement > 1M\n📎 Excel: {drive_url}"
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})
        return

    lines = [f"📊 本轮符合条件代币共 {len(tokens)} 个：\n"]
    for i, t in enumerate(tokens, 1):
        lines.append(f"""{i}. ${t['Symbol']}
   💵 价格: {t['Price']}（24h: {t['Price_24h_Change']}）
   🏅 AltRank: {t['AltRank']}
   🔥 Engagement: {t['Engagement']}（{t['Engagement_Change']}）
   🔁 Mentions: {t['Mentions']}（{t['Mentions_Change']}）""")

    lines.append(f"📎 Excel: {drive_url}")
    msg = "\n\n".join(lines)
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})