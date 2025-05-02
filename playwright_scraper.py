import asyncio
import subprocess
from playwright.async_api import async_playwright

async def save_lunarcrush_html():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://lunarcrush.com/categories/cryptocurrencies?metric=alt_rank&reverse=")
            await asyncio.sleep(10)  # 等待页面加载完成
            content = await page.content()
            with open("sample_lunarcrush.html", "w", encoding="utf-8") as f:
                f.write(content)
            await browser.close()
    except Exception as e:
        print("❌ Playwright 报错，尝试重新安装 Chromium: ", str(e))
        subprocess.run(["playwright", "install", "chromium"])
        # 重新运行脚本自身（可选）：
        subprocess.run(["python", "playwright_scraper.py"])

if __name__ == "__main__":
    asyncio.run(save_lunarcrush_html())
