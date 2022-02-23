import os
import alpaca_trade_api
from dotenv import load_dotenv

load_dotenv()

error = alpaca_trade_api.rest.APIError


class TradeBot:
    __APCA_API_KEY_ID = os.getenv('APCA_API_KEY_ID')
    __APCA_API_SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')
    __APCA_API_BASE_URL = os.getenv('APCA_API_BASE_URL')

    def __init__(self):
        self.api = alpaca_trade_api.REST(
            self.__APCA_API_KEY_ID,
            self.__APCA_API_SECRET_KEY,
            self.__APCA_API_BASE_URL,
            raw_data='raw_data',
            api_version='v2'
        )

    def get_account(self):
        try:
            account = self.api.get_account()
            return {
                'account': account
            }
        except(error):
            return {
                'error': error
            }


trade_bot = TradeBot()
