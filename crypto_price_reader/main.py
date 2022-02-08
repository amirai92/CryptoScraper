from crypto_scraper import CryptoCurrency

import time

if __name__ == '__main__':
    while True:
        smybol1 = CryptoCurrency(symbol="btcusd")
        print(smybol1.price)
        time.sleep(1)

