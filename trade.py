import os
import time
import alpaca_trade_api
from dotenv import load_dotenv

load_dotenv()

APCA_API_KEY_ID = os.getenv('APCA_API_KEY_ID')
APCA_API_SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')
APCA_API_BASE_URL = os.getenv('APCA_API_BASE_URL')


api = alpaca_trade_api.REST(
    APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, api_version='v2')

account = api.get_account()

# print(account)

try:
    # market order executes immediately, limit order will wait until a set price is reached
    order = api.submit_order(
        symbol='FB',
        side='sell',
        type='market',
        qty='2',
        time_in_force='day',
    )

    time.sleep(5)

    print(order)

except(alpaca_trade_api.rest.APIError) as e:
    print(e)
