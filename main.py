# main.py

import os
from datetime import datetime
from html_parser import extract_coin_data
from excel_exporter import save_to_excel
from drive_uploader import upload_to_drive
from telegram_notifier import send_telegram_alert

def main():
    print("[INFO] 开始执行 LunarCrush 数据处理流程")

    # STEP 1: 读取 HTML 内容
    try:
        with open("sample_lunarcrush.html", "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print("❌ 错误: 找不到 sample_lunarcrush.html 文件")
        return

    # STEP 2: 提取代币数据
    coins = extract_coin_data(html)
    print(f"[INFO] 共提取代币数量: {len(coins)}")

    # STEP 3: 写入 Excel 文件
    now = datetime.utcnow()
    excel_path = save_to_excel(coins, now)
    print(f"[INFO] Excel 已保存到: {excel_path}")

    # STEP 4: 上传到 Google Drive
    drive_url = upload_to_drive(excel_path)

    # STEP 5: Telegram 推送符合条件的代币
    send_telegram_alert(coins, drive_url)

if __name__ == "__main__":
    main()
