import os
import datetime
import pandas as pd
from html_parser import extract_coin_data
from excel_exporter import save_to_excel
from drive_uploader import upload_to_drive
from telegram_notifier import send_telegram_alert


def main():
    print("[INFO] 开始执行 LunarCrush 数据处理流程")

    # 创建时间戳用于保存和标识
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M")

    # 解析 HTML 提取数据
    coins = extract_coin_data()
    print(f"[INFO] 共提取代币数量: {len(coins)}")

    # 保存为 Excel 文件（按年月/日/小时）
    excel_path = save_to_excel(coins, date_str, time_str)
    print(f"[INFO] Excel 已保存到: {excel_path}")

    # 上传到 Google Drive（可选）
    try:
        drive_url = upload_to_drive(excel_path)
        print(f"[INFO] 已上传至 Google Drive: {drive_url}")
    except Exception as e:
        print(f"[WARNING] 上传至 Google Drive 失败: {e}")
        drive_url = None

    # 过滤满足推送条件的币种
    filtered = [c for c in coins if c.get("AltRank") and int(c["AltRank"]) <= 50 and \
                c.get("Engagement") and c.get("Engagement_Change") and \
                int(str(c["Engagement"]).replace(",", "")) > 1_000_000]

    # 发送 Telegram 推送
    if filtered:
        send_telegram_alert(filtered, date_str, time_str, excel_path, drive_url)
    else:
        send_telegram_alert([], date_str, time_str, excel_path, drive_url)


if __name__ == "__main__":
    main()
