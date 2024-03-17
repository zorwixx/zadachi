import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headers = soup.find_all(["h1", "h2", "h3"])

    for header in headers:
        print(header.text)
else:
    print(f"Не вдалося отримати сторінку. Код статусу: {response.status_code}")



