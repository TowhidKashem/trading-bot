import TradeBot
import alpaca_trade_api
import time

class BuyStock(TradeBot):
    def __init__(self):
        super().__init__()

    def buy(self, symbol, qty):
        try:
            # market order executes immediately, limit order will wait until a set price is reached
            order = self.api.submit_order(
                symbol='FB',
                side='sell',
                type='market',
                qty='2',
                time_in_force='day',
            )

            time.sleep(5)

            print(order)

        except(alpaca_trade_api.rest.APIError) as e:
            print('APIError')

buy_stock = BuyStock()
