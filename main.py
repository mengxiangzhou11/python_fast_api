from typing import Union

from fastapi import FastAPI
import requests

app = FastAPI()

#请求鱼池矿机数据
@app.get("/f2pool")
def read_root():
    url = 'https://www.f2pool.com/miners'
    data = {}
    r = requests.post(url, data=data)
    return {"status": 200,"msg": r.text}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
