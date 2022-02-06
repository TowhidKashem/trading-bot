from service.TradeBot import TradeBot
from alpaca_trade_api.stream import Stream


class StockData(TradeBot):
    def __init__(self):
        super().__init__()
        self.stream = Stream(
            self._TradeBot__APCA_API_KEY_ID,
            self._TradeBot__APCA_API_SECRET_KEY,
            self._TradeBot__APCA_API_BASE_URL,
            data_feed='iex'
        )

    def live_stream(self):
        async def trade_callback(t):
            print('trade', t)

        async def quote_callback(q):
            print('quote', q)

        self.stream.subscribe_trades(trade_callback, 'AAPL')
        self.stream.subscribe_quotes(quote_callback, 'IBM')
        self.stream.run()


stock_data = StockData()
