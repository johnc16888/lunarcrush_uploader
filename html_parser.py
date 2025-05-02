from bs4 import BeautifulSoup

def extract_coin_data(html):
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("a", href=True)

    coins = []
    for card in cards:
        try:
            name = card.select_one('[data-testid^="marketRowName_"] div[dir="auto"]:first-child').text.strip()
            symbol = card.select_one('[data-testid^="marketRowName_"] div[dir="auto"]:nth-child(2)').text.strip()

            price_div = card.find_all("div", string=lambda t: t and "$" in t)
            price = price_div[0].text.strip() if price_div else ""

            percent_changes = card.find_all("div", style=lambda s: s and "color" in s)
            price_change = percent_changes[0].text.strip() if len(percent_changes) > 0 else ""
            engagement_change = percent_changes[1].text.strip() if len(percent_changes) > 1 else ""
            altrank_change = percent_changes[2].text.strip() if len(percent_changes) > 2 else ""

            raw_texts = [div.text.strip().replace(",", "").replace("↑", "").replace("↓", "")
                         for div in card.find_all("div") if div.text.strip().replace(",", "").replace(".", "").replace("↑", "").replace("↓", "").isdigit()]

            engagement = raw_texts[-5] if len(raw_texts) >= 5 else ""
            mentions = raw_texts[-1] if len(raw_texts) >= 1 else ""

            coins.append({
                "Name": name,
                "Symbol": symbol,
                "Price": price,
                "Price_Change": price_change,
                "AltRank_Change": altrank_change,
                "Engagement": engagement,
                "Engagement_Change": engagement_change,
                "Mentions": mentions
            })
        except Exception:
            continue
    return coins
