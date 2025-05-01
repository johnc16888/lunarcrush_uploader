from bs4 import BeautifulSoup

def check_html_file(path="sample_lunarcrush.html"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print("❌ 文件未找到:", path)
        return False

    soup = BeautifulSoup(html, "html.parser")
    tokens = soup.find_all("div", class_="css-175oi2r")

    if not tokens or len(tokens) < 10:
        print("⚠️ 页面结构异常，可能不是真实网页 HTML。请检查是否为完整源码或使用 Playwright 自动刷新")
        return False

    print(f"✅ 成功加载 HTML，共发现 {len(tokens)} 个结构元素，结构看起来正常")
    return True

if __name__ == "__main__":
    check_html_file()