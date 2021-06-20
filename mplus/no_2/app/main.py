'''
1. Create database and collection/table with id, name of category
2. insert data to collectioin
3. create JSON file from data in collection
4. viewe a data from database using rekursif

'''

from typing import Optional
import uvicorn 
from fastapi import FastAPI
import dns


from routes.transaksi import router as DataRouter

app = FastAPI()

app.include_router(DataRouter, tags=["Data"], prefix="/category")

if __name__ == '__main__':
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
