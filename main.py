import websocket
import json
from utils.usdt_pairs import usdt_pairs
from loguru import logger 
logger.add("bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="w")
usdt_pairs = usdt_pairs[0:196]
percentage = 0
def on_message(ws, message):
    data = json.loads(message)
    kline =  data["k"]
    is_kline_closed = kline["x"]
    open_price      = kline["o"]
    close_price     = kline["c"]
    high_price      = kline["h"]
    low_price       = kline["l"]
    if is_kline_closed :
        if open_price > close_price and ((float(open_price)/float(close_price))-1) * 100 > 0.6 : 
            percentage = ((float(open_price)/float(close_price))-1) * 100 
            logger.info(f"SYMBOL : {kline['s']} PERCENTAGE : {percentage} %")



def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")   
    ws.send(json.dumps({"method": "SUBSCRIBE", "params": [symbol.lower()+"@kline_1m" for symbol in usdt_pairs], "id": 1}))


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
