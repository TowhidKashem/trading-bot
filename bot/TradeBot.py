import os
import alpaca_trade_api
from dotenv import load_dotenv

load_dotenv()

class TradeBot():
    __APCA_API_KEY_ID = os.getenv('APCA_API_KEY_ID')
    __APCA_API_SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')
    __APCA_API_BASE_URL = os.getenv('APCA_API_BASE_URL')

    def __init__(self):
        self.api = alpaca_trade_api.REST(
            self.__APCA_API_KEY_ID,
            self.__APCA_API_SECRET_KEY,
            self.__APCA_API_BASE_URL,
            api_version='v2'
        )

    def get_account(self):
        account = self.api.get_account()
        return account._raw


trade_bot = TradeBot()
