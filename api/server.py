from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    return {'posts': posts.json()}


@app.route('/hello', methods=['GET'])
def hello():
    return render_template("page.html")


app.run()
