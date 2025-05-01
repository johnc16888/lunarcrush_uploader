import pandas as pd
from datetime import datetime
import os

def save_to_excel(tokens):
    df = pd.DataFrame(tokens)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    folder = "./data/excel"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"filtered_lunarcrush_{timestamp}.xlsx")
    df.to_excel(path, index=False)

    def parse_number(s):
        s = s.replace(",", "").replace("K", "e3").replace("M", "e6")
        return int(float(s))

    filtered = [t for t in tokens if int(t["AltRank"]) <= 50 and parse_number(t["Engagement"]) > 1_000_000]
    return path, filtered