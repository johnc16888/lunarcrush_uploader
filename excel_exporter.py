import os
import pandas as pd

def save_to_excel(coins, now):
    if not coins:
        print("[INFO] 没有代币数据需要保存")
        return None

    # 构建多层目录结构：./data/excel/YYYY/MM/DD/HH/
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")

    folder_path = os.path.join("data", "excel", year, month, day, hour)
    os.makedirs(folder_path, exist_ok=True)

    # 文件名：filtered_lunarcrush_YYYY-MM-DD_HH-MM.xlsx
    filename = f"filtered_lunarcrush_{now.strftime('%Y-%m-%d_%H-%M')}.xlsx"
    file_path = os.path.join(folder_path, filename)

    # 保存为 Excel
    df = pd.DataFrame(coins)
    df.to_excel(file_path, index=False)

    print(f"[INFO] Excel 已保存到: {file_path}")
    return file_path
