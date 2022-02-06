from TradeBot import TradeBot
from alpaca_trade_api import rest


class BuyStock(TradeBot):
    def __init__(self):
        super().__init__()

    def buy(self):
        try:
            # market order executes immediately, limit order will wait until a set price is reached
            order = self.api.submit_order(
                symbol='FB',
                side='buy',
                type='market',
                qty='2',
                time_in_force='day',
            )

            print(order)

        except(rest.APIError) as error:
            print(error)


buy_stock = BuyStock()
