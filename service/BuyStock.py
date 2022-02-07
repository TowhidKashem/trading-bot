from service.TradeBot import TradeBot
from alpaca_trade_api import rest

error = rest.APIError


class BuyStock(TradeBot):
    def __init__(self):
        super().__init__()

    def buy(self, symbol, quantity):
        try:
            # market order executes immediately, limit order will wait until a set price is reached
            order = self.api.submit_order(
                symbol=symbol,
                side='buy',
                type='market',
                qty=quantity,
                time_in_force='day',
            )
            return {
                'receipt': order
            }
        except(error):
            print(error)


buy_stock = BuyStock()
