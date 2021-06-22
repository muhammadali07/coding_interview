from flask import Flask, json
from flask_pymongo import PyMongo
from flask import jsonify
from bson.json_util import dumps, ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/mnc"
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Backend of Python Developer'

@app.route('/check')
def check_data():
    data = mongo.db.buku.find({})
    output = []
    for x in data:
        output.append({'nama_category':x['nama_category'], 'jenis_category':x['jenis_category']})
        json_data = dumps(output, indent = 2)
        with open ('datax.json', 'w') as file:
            file.write(json_data)
    return jsonify(output)

if __name__ =='__main__':
    app.run(debug=True)
