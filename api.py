from constants import *
from flask import Flask, request, send_from_directory
from operator import itemgetter
from service.TradeBot import trade_bot
from service.BuyStock import buy_stock
from service.SellStock import sell_stock
from service.StockData import stock_data

app = Flask(__name__)


@app.route('/account', methods=['GET'])
def account():
    response = trade_bot.get_account()

    if response.get('error'):
        return {
            'account': None,
            'success': False,
            'error_code': UNKNOWN_ERROR,
            'pass_through_service_error': response['error']
        }, 500

    else:
        account_blocked, status = itemgetter(
            'account_blocked',
            'status'
        )(response['account'])

        is_blocked_or_inactive = account_blocked or status != 'ACTIVE'
        status_code = 403 if is_blocked_or_inactive else 200

        return {
            'account': response['account'] if not is_blocked_or_inactive else None,
            'success': True
        }, status_code


@app.route('/buy', methods=['POST'])
def buy_stock():
    args = request.get_json()
    required_args = ['symbol', 'quantity']

    if not args or not all(arg in args for arg in required_args):
        return {
            'success': False,
            'error_code': INVALID_ARGUMENTS
        }, 400

    purchase = buy_stock.buy(args['symbol'], args['quantity'])

    return {
        'success': True,
        'receipt': purchase
    }, 200


@app.route('/sell', methods=['POST'])
def sell_stock():
    sell = sell_stock.sell()
    return {
        'success': sell
    }


@app.route('/live-stream', methods=['GET'])
def live_stream():
    stream = stock_data.live_stream()
    return {
        'stream': stream
    }


# temp: for testing
@app.route('/page', methods=['GET'])
def home():
    return send_from_directory('views', 'index.html')


app.run()
