# run_all.py

import subprocess
from html_checker import is_valid_lunarcrush_html
from main import main

def run_playwright_scraper():
    print("🚀 [STEP] 自动刷新并抓取 LunarCrush 页面...")
    try:
        subprocess.run(["python", "playwright_scraper.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Playwright 执行失败: {e}")
        return False
    return True

def check_html_structure():
    print("🚀 [STEP] 检查抓取 HTML 文件结构...")
    try:
        with open("sample_lunarcrush.html", "r", encoding="utf-8") as f:
            html = f.read()
        valid = is_valid_lunarcrush_html(html)
        if not valid:
            print("⚠️ 页面中未检测到代币卡片结构")
            print("⚠️ 页面结构异常，继续执行主流程（将尝试提取可能的内容）")
        return True
    except Exception as e:
        print(f"❌ HTML 文件读取失败: {e}")
        return False

def run_main_script():
    print("🚀 [STEP] 运行主流程提取 + Excel + Drive + Telegram...")
    try:
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 主流程执行失败: {e}")

if __name__ == "__main__":
    if run_playwright_scraper():
        check_html_structure()
        run_main_script()
    print("✅ 所有步骤执行完成。")
