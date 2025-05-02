import os
import subprocess

# Step 1: Use Playwright to fetch the latest HTML
def run_playwright_scraper():
    print("\n\U0001F680 [STEP 1] 自动刷新并抓取 LunarCrush 页面...")
    try:
        subprocess.run(["python", "playwright_scraper.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("\u274c Playwright 执行失败:", e)

# Step 2: Check the HTML structure
def run_html_checker():
    print("\U0001F50D [STEP 2] 检查抓取 HTML 文件结构...")
    try:
        subprocess.run(["python", "html_checker.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("\u274c HTML 检查失败:", e)

# Step 3: Main pipeline - parse + Excel + Drive + Telegram
def run_main():
    print("\U0001F4CA [STEP 3] 运行主流程提取 + Excel + Drive + Telegram...")
    try:
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("\u274c 主流程执行失败:", e)

if __name__ == "__main__":
    run_playwright_scraper()
    run_html_checker()
    run_main()
    print("\u2705 所有步骤执行完成。")
