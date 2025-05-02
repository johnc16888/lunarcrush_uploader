# run_all.py

import subprocess
import os
from html_checker import is_valid_lunarcrush_html

def step(title):
    print(f"\n🚀 [STEP] {title}...")

def run_command(script):
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 执行 {script} 失败:", e)

if __name__ == "__main__":
    # STEP 1: Playwright 抓取网页
    step("自动刷新并抓取 LunarCrush 页面")
    result = subprocess.run(["python", "playwright_scraper.py"])
    if result.returncode != 0:
        print("❌ Playwright 执行失败: ", result)

    # STEP 2: 检查 HTML 文件结构
    step("检查抓取 HTML 文件结构")
    valid = is_valid_lunarcrush_html()
    if not valid:
        print("⚠️ 页面结构异常，继续执行主流程（将尝试提取可能的内容）")

    # STEP 3: 主流程：提取数据 + 存 Excel + 上传 Drive + 推送 Telegram
    step("运行主流程提取 + Excel + Drive + Telegram")
    try:
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 主流程执行失败: {e}")

    print("✅ 所有步骤执行完成。")
