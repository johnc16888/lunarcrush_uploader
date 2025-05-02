# html_checker.py

from bs4 import BeautifulSoup

def is_valid_lunarcrush_html(html: str) -> bool:
    """检查 HTML 是否包含有效的 LunarCrush 代币卡片结构"""
    soup = BeautifulSoup(html, "html.parser")
    # 查找是否至少存在一个卡片结构
    return soup.find("div", {"data-testid": "coin-card"}) is not None
