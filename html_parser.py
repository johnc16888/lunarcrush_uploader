from bs4 import BeautifulSoup

def extract_all_tokens():
    with open("sample_lunarcrush.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    # TODO: Replace with real parsing
    return [{
        "Name": "Akash Network",
        "Symbol": "AKT",
        "Price": "$1.71",
        "Price_24h_Change": "-0.14%",
        "AltRank": 1,
        "Engagement": "1,230,000",
        "Engagement_Change": "+59,500",
        "Mentions": "2,300",
        "Mentions_Change": "+629",
        "Trading Volume": "$204.42M"
    }]