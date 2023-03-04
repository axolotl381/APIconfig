from fastapi import FastAPI
import datetime

import gmo

app = FastAPI()


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
