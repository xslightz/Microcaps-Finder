import urllib2, json
url = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker')
obj = json.load(url)

def get_coins():
    for row in obj:
        if (int(float(row['market_cap_usd']))	< 250000000): #if coin is less than $250,000,000 market cap
            if (float(row['total_supply']) < 50000000): # if coin is less than 50,000,000 total supply
                print "Name:", row['name']
                print "Symbol:", row['symbol']
                print "BTC:", row['price_btc']
                print "Volume (24h):", "{:,}".format(float(row['24h_volume_usd']));
                print "Market Cap:", "{:,}".format(float(row['market_cap_usd']));
                print "Supply:","{:,}".format(float(row['total_supply']));
                print "Circulating Supply:", "{:,}".format(float(row['available_supply']));
                print "% Change (24hr):", row['percent_change_24h']
                print ""
if __name__ == "__main__":
    get_coins()
raw_input('press any key to close')