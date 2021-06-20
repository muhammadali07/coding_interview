from json import dump
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.model_data import *
from bson.json_util import dumps, loads
import connection

router = APIRouter()

@router.post("/post_data/{nama_category}/{jenis_category}", tags=["Data"])
def post_data(nama_category:str, jenis_category : str):
    try:
        if connection.db.category.find({'nama_category' : nama_category}):
            connection.db.category.insert_one({'nama_category' : nama_category, 'jenis_category': jenis_category})
            return{"message" : "data berhasil ditambahkan"}
        else:
            return{"message" : "data kosong"}
    except Exception:
        return post_data

@router.get("/view_data", tags=["Data"])
def view_data():
    col = connection.db.category
    output = []
    for x in col.find({}):
        output.append({'nama category': x['nama_category'], 'jenis category':x['jenis_category']})
        json_data = dumps(output, indent = 2)
        with open('list_data_category.json', 'w') as file:
            file.write(json_data)
    return JSONResponse({'result': output})

@router.get('/rekursif_data', tags=["Data"])
def rekursif_data():
    res = connection.db.category.find({})
    data = int(res.count())
    x = []
    try:
        if connection.db.category.find_one({}):
            col = connection.db.category.find_one({})
            x.append({'nama':col['nama_category'], 'jenis kategory':col['jenis_category']})
            return JSONResponse({'result':x})
    except Exception:
        return rekursif_data

