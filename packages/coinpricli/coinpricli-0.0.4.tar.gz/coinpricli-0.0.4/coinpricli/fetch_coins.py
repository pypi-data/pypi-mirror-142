from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
default_parameter = {'limit': 5}


def fetch_crypto_data(options=default_parameter):
    data = []
    res = requests.get(url)
    res.encoding = "utf-8"

    if res.status_code != 200:
        print("Fail to Fetch Coins")

    soup = BeautifulSoup(res.text, 'html.parser')
    tables = soup.find('table')

    coins = tables.tbody.find_all('tr')

    for coin in coins[0:options['limit']]:
        cells = coin.find_all('td')
        symbol = dict()
        symbol_tags = cells[2].find_all('p')
        symbol['name'] = symbol_tags[0].getText()
        symbol['symbol'] = symbol_tags[1].getText()

        # price
        symbol['price'] = cells[3].find('span').getText()

        # 24h change
        symbol['today_change'] = cells[4].find('span').getText()

        # weekly change
        symbol['week_change'] = cells[5].find('span').getText()

        # weekly change
        symbol['market_cap'] = cells[6].find('span').getText()

        volume_tags = cells[7].find_all('p')
        symbol['volume_in_fiat'] = volume_tags[0].getText()
        symbol['volume'] = volume_tags[1].getText()

        symbol['chart'] = cells[9].find('img')['src']
        data.append(symbol)
    return data

# print(fetch_crypto())
