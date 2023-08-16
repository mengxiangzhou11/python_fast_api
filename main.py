from typing import Union

from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#请求鱼池矿机数据
@app.get("/f2pool")
def read_root():
    url = 'https://www.f2pool.com/miners'
    data = {}
    r = requests.post(url, data=data)
    return {"status": 200,"msg": r.text}

#请求鱼池矿机数据
@app.get("/lbc")
def read_root():

    ##########################################登录#########################################################
    data = {
        'account': '86.15370406510',
        'password': 'a123456789'
    }

    headers = {'Content-Type': 'application/json'}

    res = requests.post(url='https://www.dxpool.com/api/v2/users/login', headers=headers, data=json.dumps(data))
    res_value = json.loads(res.text)
    token = res_value['token']

    ##########################################请求lbc旷工列表#########################################################
    data = {
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'authorization': 'Bearer '+token,
    }

    res = requests.post(url='https://www.dxpool.com/api/pools/lbc/accounts/6783/miners?group_id=7679&status=0&page_size=20&offset=0', headers=headers, data=data)


    return {"status": 200,"msg": res.text,"token": headers}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
