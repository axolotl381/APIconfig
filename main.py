from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import datetime

import gmo

app = FastAPI()


class OrderParam(BaseModel):
    Symbol:str
    Side:str
    Price:str
    Size:str

class Item(BaseModel):
    name:str
    price:int



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test2():
    return {"message":"abc"}

@app.get("/time")
async def test():
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    return {"message": now}

@app.get("/items/{number}")
async def read_item(number:int):
    return {"item_id": number}

@app.get("/gmo/margin")
async def getMargin():
    result = gmo.gmoGetMargin()
    return result

@app.get("/gmo/tradingVolume")
async def getTradingVolume():
    result = gmo.gmoGetTradingVolume()
    return result

@app.get("/gmo/orderInfo/{orderId}")
async def getOrderInfo(orderId:int):
    result = gmo.gmoGetOrderInfo(orderId)
    return result

# example curl cli with json param.
# curl -X POST -H "accept: application/json" -H "Content-Type: application/json"  -d '{"Symbol":"XRP", "Side":"BUY","Price":"48","Size":"1"}' http://u-pa.mydns.jp/api/gmo/order
@app.post("/gmo/order")
async def postOrder(orderParam:OrderParam):
    result = gmo.gmoPostOrder(orderParam.Symbol,orderParam.Side,orderParam.Price,orderParam.Size)
    return result

@app.post("/test/post")
async def users(item:Item):
    return item
