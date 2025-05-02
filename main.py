# main.py

from excel_exporter import save_to_excel
from html_parser import parse_lunarcrush_html
from drive_uploader import upload_to_drive
from telegram_notifier import notify_results
import os

def main():
    print("[INFO] 开始执行 LunarCrush 数据处理流程")

    # Step 1: 解析 HTML
    try:
        parsed_data, filtered_data = parse_lunarcrush_html("sample_lunarcrush.html")
        print(f"[INFO] 共提取代币数量: {len(parsed_data)}")
    except Exception as e:
        print(f"[ERROR] HTML 解析失败: {e}")
        return

    # Step 2: 保存 Excel
    try:
        excel_path = save_to_excel(parsed_data, filtered_data)
        print(f"[INFO] Excel 已保存到: {excel_path}")
    except Exception as e:
        print(f"[ERROR] Excel 保存失败: {e}")
        return

    # Step 3: 上传至 Google Drive
    try:
        drive_url = upload_to_drive(excel_path)
    except Exception as e:
        print(f"[ERROR] 上传 Google Drive 失败: {e}")
        drive_url = None

    # Step 4: 推送 Telegram
    try:
        notify_results(filtered_data, drive_url)
    except Exception as e:
        print(f"[ERROR] Telegram 推送失败: {e}")

if __name__ == "__main__":
    main()
