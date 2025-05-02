# html_checker.py

def is_valid_html(html_content: str) -> bool:
    """
    简单检查 HTML 页面中是否包含 LunarCrush 的代币卡片结构。
    可根据 'data-testid="coin-card"' 等特征进行判断。
    """
    if not html_content:
        return False
    return "coin-card" in html_content or "data-testid=\"coin-card\"" in html_content
