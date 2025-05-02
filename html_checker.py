# html_checker.py

from bs4 import BeautifulSoup

def is_valid_lunarcrush_html(html_path="sample_lunarcrush.html") -> bool:
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        
        # 检查是否包含常见的代币卡片结构（根据 Akash Network 样例）
        cards = soup.select("div.flex.flex-col.bg-card.rounded-xl")
        if len(cards) == 0:
            print("⚠️ 页面中未检测到代币卡片结构")
            return False
        
        # 检查是否包含代币名/代码字段
        sample = cards[0]
        has_name = sample.select_one("p.text-base.font-semibold")
        has_symbol = sample.select_one("p.text-xs.uppercase.text-subtitle")
        if not has_name or not has_symbol:
            print("⚠️ 页面结构存在，但未检测到代币名称或代码")
            return False
        
        print("✅ 页面结构看起来正常")
        return True
    except Exception as e:
        print("❌ HTML 检查失败:", str(e))
        return False

if __name__ == "__main__":
    is_valid_lunarcrush_html()
