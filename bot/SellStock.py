import TradeBot
import alpaca_trade_api

class SellStock(TradeBot):
    def __init__(self):
        super().__init__()

    def sell(self, symbol, qty):
        pass

sell_stock = SellStock()
