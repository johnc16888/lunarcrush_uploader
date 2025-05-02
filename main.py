import os
from datetime import datetime
from html_parser import extract_coin_data
from excel_exporter import save_to_excel
from telegram_notifier import send_telegram_alert
from drive_uploader import upload_to_drive
from playwright_scraper import save_lunarcrush_html

def main():
    now = datetime.utcnow()
    print("✅ 已成功写入 credentials.json")

    print("🚀 [STEP 1] 自动刷新并抓取 LunarCrush 页面...")
    save_lunarcrush_html()

    print("🔍 [STEP 2] 检查抓取 HTML 文件结构...")
    try:
        with open("sample_lunarcrush.html", "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print("❌ 找不到 sample_lunarcrush.html 文件")
        return

    coins = extract_coin_data(html)
    print(f"[INFO] 共提取代币数量: {len(coins)}")

    if not coins:
        print("[INFO] 没有代币数据需要保存")
        excel_path = None
    else:
        excel_path = save_to_excel(coins, now)
        print(f"[INFO] Excel 已保存到: {excel_path}")

    # 🧪 调试环境变量
    print("[DEBUG] 是否设置 GOOGLE_SERVICE_ACCOUNT_JSON:", "GOOGLE_SERVICE_ACCOUNT_JSON" in os.environ)

    # 上传到 Google Drive（可选）
    if excel_path:
        try:
            drive_url = upload_to_drive(excel_path)
            print(f"[INFO] 文件上传成功: {drive_url}")
        except Exception as e:
            print(f"[ERROR] 上传到 Google Drive 出错: {e}")

    # 推送 Telegram（只推送满足条件的代币）
    send_telegram_alert(coins, excel_path)

if __name__ == "__main__":
    main()
