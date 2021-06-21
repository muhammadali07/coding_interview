from flask import Flask
import pymongo
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello word'

if __name__ =='__main__':
    app.run(debug=True)
