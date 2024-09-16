import requests
import json
import hmac
import hashlib
import time
from datetime import datetime



API_KEY="82JR1clDAsLc+WH/Fxyje2srCVq5ikI0"
SECRET_KEY="MdGX30hGQ5iV6o4gXk0SFPoOrHXYRjsMy+dvWwR0P97cWo+vuD6EbrHJZmVNVhmC"



def gmoGetMargin():


    apiKey = API_KEY
    secretKey = SECRET_KEY

    timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
    # timestamp ="1677914724000"
    method    = 'GET'
    endPoint  = 'https://api.coin.z.com/private'
    path      = '/v1/account/margin'

    text = timestamp + method + path
    print(bytes(secretKey.encode('ascii')))
    print("★")
    sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
    print(sign)

    headers = {
        "API-KEY": apiKey,
        "API-TIMESTAMP": timestamp,
        "API-SIGN": sign
    }

    res = requests.get(endPoint + path, headers=headers)
    return res.json()

def gmoGetTradingVolume():
    apiKey    = API_KEY
    secretKey = SECRET_KEY

    timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
    method    = 'GET'
    endPoint  = 'https://api.coin.z.com/private'
    path      = '/v1/account/tradingVolume'

    text = timestamp + method + path
    sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()

    headers = {
        "API-KEY": apiKey,
        "API-TIMESTAMP": timestamp,
        "API-SIGN": sign
    }

    res = requests.get(endPoint + path, headers=headers)
    jpyVolume =  res.json()['data']['jpyVolume']
    tierLevel =  res.json()['data']['tierLevel']
    return {"jpyVolume":jpyVolume,"tierLevel":tierLevel}

def gmoGetOrderInfo(Id:int):
    apiKey    = API_KEY
    secretKey = SECRET_KEY

    orderId = str(Id)

    timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
    method    = 'GET'
    endPoint  = 'https://api.coin.z.com/private'
    path      = '/v1/orders'

    text = timestamp + method + path
    sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
    parameters = { "orderId": orderId }

    headers = {
        "API-KEY": apiKey,
        "API-TIMESTAMP": timestamp,
        "API-SIGN": sign
    }

    res = requests.get(endPoint + path, headers=headers, params=parameters)
    return res.json()


def gmoPostOrder(symbol:str,side:str,price:str,size:str):
    apiKey    = API_KEY
    secretKey = SECRET_KEY

    timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
    method    = 'POST'
    endPoint  = 'https://api.coin.z.com/private'
    path      = '/v1/order'
    reqBody = {
        "symbol": symbol,
        "side": side,
        "executionType": "LIMIT",
        "timeInForce": "FAS",
        "price": price,
        "size": size
    }

    text = timestamp + method + path + json.dumps(reqBody)
    sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()

    headers = {
        "API-KEY": apiKey,
        "API-TIMESTAMP": timestamp,
        "API-SIGN": sign
    }

    res = requests.post(endPoint + path, headers=headers, data=json.dumps(reqBody))
    orderId = 0
    status = res.json()["status"]
    if status == 0:
            orderId =  res.json()["data"]
    else:
            orderId = status
    return { "orderId": orderId }

def gmoPostCancelOrder(Id:int):
    apiKey    = API_KEY
    secretKey = SECRET_KEY

    orderId = str(Id)

    timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
    method    = 'GET'
    endPoint  = 'https://api.coin.z.com/private'
    path      = '/v1/cancelOrder'

    reqBody = {
            "orderId": orderId
    }

    text = timestamp + method + path + json.dumps(reqBody)
    sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()

    headers = {
        "API-KEY": apiKey,
        "API-TIMESTAMP": timestamp,
        "API-SIGN": sign
    }
    
    orderId = 0
    status = res.json()["status"]
    if status == 0:
            orderId =  res.json()["data"]
    else:
            orderId = status
    return { "orderId": orderId }



