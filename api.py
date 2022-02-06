from flask import Flask, jsonify
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
            'message': response['error']
        }, 500
    else:
        account = response['account']
        status = 403 if account['account_blocked'] or account['status'] != 'ACTIVE' else 200
        return {
            'account': response['account'],
            'success': True
        }, status


@app.route('/live-stream', methods=['GET'])
def live_stream():
    stream = stock_data.live_stream()
    return {
        'stream': stream
    }


@app.route('/buy', methods=['POST'])
def buy_stock():
    buy = buy_stock.buy()
    return {
        'success': buy
    }


@app.route('/sell', methods=['POST'])
def sell_stock():
    sell = sell_stock.sell()
    return {
        'success': sell
    }


app.run()
