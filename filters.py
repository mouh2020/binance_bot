from binance.helpers import round_step_size
from binance.client import Client

client = Client()

def quantity (symbol,balance,price) :
    return round_step_size(float(balance)/float(price), client.get_symbol_info(symbol)["filters"][2]["stepSize"])
    
def price (symbol,price) :
    return round_step_size(float(price), client.get_symbol_info(symbol)["filters"][0]["tickSize"])
