from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import trading_bot

load_dotenv()

app = Flask(__name__)


@app.route('/account', methods=['GET'])
def account():
    account = trade_bot.get_account()
    return {
        'account': account._raw
    }


app.run()
