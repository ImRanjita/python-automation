from bs4 import BeautifulSoup
import requests

def getCurrency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    print(url)
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')

    rate = soup.find("span", class_="ccOutputTrail").get_text()
    rate = float(rate[:4])

    return rate

currency = getCurrency("EUR", "USD")
print (currency)
