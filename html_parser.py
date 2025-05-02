from bs4 import BeautifulSoup


def extract_coin_data(html):
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="chakra-card")

    coins = []
    for card in cards:
        try:
            name = card.find("div", class_="css-15c1g3n").text.strip()
            symbol = card.find("div", class_="css-1r7ky0e").text.strip()
            price = card.find("div", class_="css-1j8o68f").text.strip()
            price_change = card.find("div", class_="css-1b7nvhl").text.strip()
            alt_rank = card.find("div", class_="css-1lkkvye").text.strip()

            mentions_raw = card.find("div", string="Mentions").find_next("div").text.strip()
            mention_change_raw = card.find("div", string="Mentions").find_next("div").find_next("div").text.strip()

            engagement_raw = card.find("div", string="Engagement").find_next("div").text.strip()
            engagement_change_raw = card.find("div", string="Engagement").find_next("div").find_next("div").text.strip()

            def convert_abbreviated_number(num_str):
                num_str = num_str.replace(",", "")
                if "K" in num_str:
                    return int(float(num_str.replace("K", "")) * 1_000)
                elif "M" in num_str:
                    return int(float(num_str.replace("M", "")) * 1_000_000)
                elif "B" in num_str:
                    return int(float(num_str.replace("B", "")) * 1_000_000_000)
                return int(float(num_str))

            coin = {
                "Name": name,
                "Symbol": symbol,
                "Price": price,
                "Price_Change": price_change,
                "AltRank": int(alt_rank.replace("#", "")),
                "Mentions": convert_abbreviated_number(mentions_raw),
                "Mentions_Change": mention_change_raw,
                "Engagement": convert_abbreviated_number(engagement_raw),
                "Engagement_Change": engagement_change_raw
            }

            coins.append(coin)
        except Exception as e:
            print(f"❌ 跳过异常卡片: {e}")

    return coins
