from flask import Flask, jsonify
import os
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://192.168.99.100:27017/mplus"
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'hello word'

@app.route('/check_data')
def check_data():
    data = mongo.db.category.find({})
    for x in data:
        return jsonify({'nama category':x['nama_category']})

if __name__ =='__main__':
    app.run(debug=True)
