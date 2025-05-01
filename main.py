from html_parser import extract_all_tokens
from excel_exporter import save_to_excel
from drive_uploader import upload_to_drive
from telegram_notifier import send_telegram_summary

def main():
    print("[INFO] 开始执行 LunarCrush 数据处理流程")

    all_tokens = extract_all_tokens()
    print(f"[INFO] 共提取代币数量: {len(all_tokens)}")

    excel_path, filtered_tokens = save_to_excel(all_tokens)
    print(f"[INFO] Excel 已保存到: {excel_path}")

    drive_url = upload_to_drive(excel_path)
    print(f"[INFO] 已上传至 Google Drive: {drive_url}")

    send_telegram_summary(filtered_tokens, drive_url)
    print("[INFO] Telegram 推送已完成")

if __name__ == "__main__":
    main()