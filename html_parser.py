import os
from bs4 import BeautifulSoup

def extract_coin_data(html):
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="box-card")
    coins = []

    for card in cards:
        try:
            name = card.select_one(".coin-name").text.strip()
            symbol = card.select_one(".coin-symbol").text.strip()
            price = card.select_one(".price").text.strip()
            price_change = card.select_one(".percent-change").text.strip()
            altrank = card.select_one(".altrank .value").text.strip()
            engagement = card.select_one(".engagement .value").text.strip()
            engagement_change = card.select_one(".engagement .change").text.strip()
            mentions = card.select_one(".mentions .value").text.strip()
            mentions_change = card.select_one(".mentions .change").text.strip()

            coins.append({
                "Name": name,
                "Symbol": symbol,
                "Price": price,
                "Price_Change": price_change,
                "AltRank": altrank,
                "Engagement": engagement,
                "Engagement_Change": engagement_change,
                "Mentions": mentions,
                "Mentions_Change": mentions_change
            })
        except Exception:
            continue

    return coins
