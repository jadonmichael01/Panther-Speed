from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from flask_cors import CORS
import pymongo
from bson import json_util

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017)

db = client.flask_db
wifi = client.wifi_result
todos = db.todos
result = wifi.results

@app.route('/', methods=('GET', 'POST'))
def index():
    data = result.find().sort("_id",-1).limit(1)
    return json_util.dumps(data)


@app.route('/all', methods=('GET', 'POST'))
def index_all():
    data = result.find().sort("_id",-1).limit(10)
    return json_util.dumps(data)


