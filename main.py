from typing import Union

from fastapi import FastAPI
import requests

app = FastAPI()

#
@app.get("/")
def read_root():
    url = 'https://www.f2pool.com/miners'
    data = {}
    r = requests.post(url, data=data)
    return {"Hello": "World","Hello11": r.text}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
