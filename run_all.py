import os

# 确保 Playwright 浏览器环境存在
os.system("playwright install chromium")

# 生成 Google Drive 凭证
os.system("python generate_credentials.py")

# 启动主流程
os.system("python playwright_scraper.py")
os.system("python html_checker.py")
os.system("python main.py")