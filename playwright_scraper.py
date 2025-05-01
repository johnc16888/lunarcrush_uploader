import asyncio
from playwright.async_api import async_playwright

async def save_lunarcrush_html():
    url = "https://lunarcrush.com/categories/cryptocurrencies?metric=alt_rank&reverse="
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(8000)  # 等待 JS 完整渲染（8秒）

        # 可滚动以加载更多（可选）
        await page.mouse.wheel(0, 3000)
        await page.wait_for_timeout(2000)

        content = await page.content()
        with open("sample_lunarcrush.html", "w", encoding="utf-8") as f:
            f.write(content)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(save_lunarcrush_html())