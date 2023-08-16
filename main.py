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
    data = {
        'account': '86.15370406510',
        'password': 'a123456789'
    }

    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}

    ## post的时候，将data字典形式的参数用json包转换成json格式。
    res = requests.post(url='https://www.dxpool.com/api/v2/users/login', headers=headers, data=json.dumps(data))
    res_value = json.loads(res.text)
    return {"status": 200,"msg": res.text,"token": res_value['token']}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
