import requests
from datetime import datetime

# === CMP Scraper from NSE ===
def get_nse_cmp(symbol):
    url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}"
    }

    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['priceInfo']['lastPrice']
        else:
            return "⚠️ Not found"
    except Exception as e:
        return "⚠️ Error"

# === Define Your Stocks Here ===
elite_stocks = {
    "SOLARINDS": "Solar Industries",
    "MAZDOCK": "Mazagon Dock",
    "KPIGREEN": "KPI Green Energy",
    "RPOWER": "RPower"
}

today = datetime.now().strftime("%d %B %Y")
content = f"🔥 Elite Breakout Stocks – {today}\n\n"

for symbol, name in elite_stocks.items():
    cmp = get_nse_cmp(symbol)
    content += f"{name} – ₹{cmp}\n"
    content += "- Pattern: (VCP / Rocket / Flat)\n"
    content += "- Sector: (e.g., Energy)\n"
    content += "✅/⚠️ Backed by Sector\n\n"

with open("elite.txt", "w") as f:
    f.write(content)

print("✅ elite.txt generated successfully.")
