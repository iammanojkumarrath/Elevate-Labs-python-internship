import requests
from bs4 import BeautifulSoup


url = "https://www.bbc.com/news"
response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    headlines = []
    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)
    
    
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, start=1):
            f.write(f"{i}. {headline}\n")
    
    print(f"✅ Scraping complete! {len(headlines)} headlines saved to headlines.txt")
else:
    print("❌ Failed to retrieve the webpage")
