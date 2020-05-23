import robin_stocks as rs
import pandas as pd
import requests
import config
import websocket
import threading


def on_message(ws, message):
    print(message)
    # pass


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


def start_socket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={config.finnhubToken}",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


if __name__ == "__main__":
    realTimeDataThread = threading.Thread(
        target=start_socket, name='Real Time Stock Data')
    realTimeDataThread.start()
    # threading.active_count()
    # try:
    #     r = requests.get(
    #         f'https://finnhub.io/api/v1/stock/profile2?symbol=AAPL&token={config.finnhubToken}')
    #     print(r.json())
    # except:
    #     print('')


# rs.login(config.username, config.password)
# my_stocks = rs.build_holdings()
# for key, value in my_stocks.items():
#     print(key, value)

# price: current market price
# quantity: your stock quantity
# average_buy_price: your average buy price
# percent_change: ((current market price - your average buy price) / your average buy price) * 100
# pe_ratio: P/E (Price to Earning) ratio (https://www.investopedia.com/terms/p/price-earningsratio.asp)
