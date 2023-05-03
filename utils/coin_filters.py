from binance.client import Client
client = Client()
def get_coins(targeted_symbol : str) : 
    exchange_info = client.get_exchange_info()
    targeted_pairs = []
    for symbol in exchange_info["symbols"] : 
        if symbol["quoteAsset"] == targeted_symbol.upper() and "UP" not in symbol["symbol"] and "DOWN" not in symbol["symbol"]:
            targeted_pairs.append(symbol["symbol"])
    
    return targeted_pairs