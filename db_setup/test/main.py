from fastapi import FastAPI
from fastapi.responses import UJSONResponse
import json
from fastapi.encoders import jsonable_encoder
app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Welcome to the world of FastAPI!"}

# @app.get("/brand/{brand}/data/{data}/ip/{ip}")
# async def read_user_item(brand, data, ip):
#     brand = jsonable_encoder(brand)
#     return  {"brand": brand, "data": data, "ip": ip}


@app.get("/brand/{brand}")
async def read_item(brand: str):

    return {"brand": brand}


# uvicorn main:app --reload