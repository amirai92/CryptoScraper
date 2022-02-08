from crypto_scraper import CryptoCurrency
import time
import os

if __name__ == '__main__':
    while True:
        smybol1 = CryptoCurrency(symbol="btcusd")
        smybol2 = CryptoCurrency(symbol="ethusd")
        smbol3 = CryptoCurrency(symbol='dogeusdt')

        CryptoCurrency.show_prices()
        time.sleep(3)
        CryptoCurrency.clean_prices()
        os.system("cls")
