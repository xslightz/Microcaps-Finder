import requests

c = requests.session()
url = "https://api.coinmarketcap.com/v1/ticker"

MAX_MARKET_CAP = 250000000
MAX_SUPPLY = 50000000

def get_coins():
    res = c.get(url)
    if res.status_code != 200:
        print "WARNING: Status code is not 200 - " + url

    for row in res.json():
        if (float(row['market_cap_usd']) < MAX_MARKET_CAP and float(
                row['total_supply']) < MAX_SUPPLY):  # if coin is less than $250,000,000 market cap
            print "Name:", row['name']
            print "Symbol:", row['symbol']
            print "BTC:", row['price_btc']
            print "Volume (24h):", "{:,}".format(float(row['24h_volume_usd']))
            print "Market Cap:", "{:,}".format(float(row['market_cap_usd']))
            print "Supply:", "{:,}".format(float(row['total_supply']))
            print "Circulating Supply:", "{:,}".format(float(row['available_supply']))
            print "% Change (24hr):", row['percent_change_24h']
            print ""


if __name__ == "__main__":
    try:
        get_coins()
    except Exception as e:
        print "ERROR: Couldn't get coins... Exception: " + str(e)

    raw_input('press any key to close')
