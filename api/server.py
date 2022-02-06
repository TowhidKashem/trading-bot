import sys
from pathlib import Path
sys.path.append('{ROOT_DIR}/'.format(ROOT_DIR=Path(__file__).parent.parent))
from TradeBot import trade_bot, buy_stock, sell_stock
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/account', methods=['GET'])
def account():
    account = trade_bot.get_account()
    return {
        'account': account
    }


@app.route('/buy', methods=['POST'])
def buy_stock():
    account = buy_stock.buy()
    return {
        'account': account
    }


app.run()
