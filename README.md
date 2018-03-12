# Microcaps-Finder
find microcaps using coinmarket API

I was reading [this tutorial]( https://medium.com/@daytradernik/picking-out-microcaps-101-2215a5782691) on how to spot microcaps using coinmarketcap.com I realized doing it manually would take me a lot of time since there are too many coins to look at, even by organizing them from high to low as the tutorial explains. I decided to write this small snippet to help me find these coins. Obviously, the code can be modified to any quantity you desire. I did it using Python 2.7.14 but it probably works on python3 since no special modules or code was written strictly for python2.

## Requirements

    sudo easy_install -U requests
    or 
    sudo pip install requests
    
    Python 2.7
        import requests


## Usage

    python coinmarkcap.py
    
sample output:

```
Name: Bitcore
Symbol: BTX
BTC: 0.00127274
Volume (24h): 1,835,870.0
Market Cap: 140,935,721.0
Supply: 16,846,456.0
Circulating Supply: 12,047,024.0
% Change (24hr): 3.05
```
