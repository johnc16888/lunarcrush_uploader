# playwright_scraper.py

import asyncio
from playwright.async_api import async_playwright
import subprocess

# 确保 Chromium 安装（Render 每次运行环境是临时的）
subprocess.run(["playwright", "install", "chromium"], check=True)

async def save_lunarcrush_html():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://lunarcrush.com/categories/cryptocurrencies?metric=alt_rank&reverse=")
        await page.wait_for_timeout(8000)  # 等待页面 JS 加载完成
        content = await page.content()
        with open("sample_lunarcrush.html", "w", encoding="utf-8") as f:
            f.write(content)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(save_lunarcrush_html())
