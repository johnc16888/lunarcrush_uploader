# main.py

import os
import subprocess
from html_checker import is_valid_html
from html_parser import extract_coin_data
from excel_exporter import save_to_excel
from drive_uploader import upload_to_drive
from telegram_notifier import send_telegram_alert

def main():
    print("🚀 [STEP] 自动刷新并抓取 LunarCrush 页面...")
    try:
        subprocess.run(["python", "playwright_scraper.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Playwright 报错，尝试重新安装 Chromium: {e}")
        print("⚠️ 页面结构异常，可能不是真实网页 HTML。请检查是否为完整源码或使用 Playwright 自动刷新")

    print("🚀 [STEP] 检查抓取 HTML 文件结构...")
    with open("sample_lunarcrush.html", "r", encoding="utf-8") as f:
        html = f.read()
    if not is_valid_html(html):
        print("⚠️ 页面中未检测到代币卡片结构")
        print("⚠️ 页面结构异常，继续执行主流程（将尝试提取可能的内容）")

    print("🚀 [STEP] 运行主流程提取 + Excel + Drive + Telegram...")
    coins = extract_coin_data(html)
    print(f"[INFO] 共提取代币数量: {len(coins)}")

    if not coins:
        print("[INFO] 没有代币数据需要保存")
        excel_path = None
    else:
        excel_path = save_to_excel(coins)
        print(f"[INFO] Excel 已保存到: {excel_path}")

    try:
        if excel_path:
            drive_url = upload_to_drive(excel_path)
        else:
            drive_url = None
    except Exception as e:
        print(f"[ERROR] 上传到 Google Drive 失败: {e}")
        drive_url = None

    try:
        send_telegram_alert(coins, excel_path)
    except Exception as e:
        print(f"[ERROR] 推送 Telegram 失败: {e}")

    print("✅ 所有步骤执行完成。")

if __name__ == "__main__":
    main()
