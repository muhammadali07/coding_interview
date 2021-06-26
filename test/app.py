from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://172.20.0.2:27017/mnc"
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'this test'

@app.route('/view')
def view():
    data = mongo.db.buku.find({})
    out = []
    for x in data:
        out.append({'name_caterogy':x['name_category']})
    return jsonify({'result':out})

if __name__=='__main':
    app.run(debug=True)