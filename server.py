from flask import Flask, render_template, request, jsonify
from TradeBot import trade_bot
from BuyStock import buy_stock
from SellStock import sell_stock

app = Flask(__name__)


@app.route('/account', methods=['GET'])
def account():
    account = trade_bot.get_account()
    return {
        'account': account
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
