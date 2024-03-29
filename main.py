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

#coinex 实时价格
@app.get("/coinex/price/{item_id}")
def read_root(item_id: str):
    url = f"https://www.coinex.com/res/vote2/project/{item_id}"
    data = {}
    r = requests.get(url, data=data)
    return {"status": 200,"msg": r.text}

#coinex 实时价格
@app.get("/xt/price/{item_id}")
def read_root(item_id: str):
    url = f"https://www.xt.com/sapi/v4/market/public/ticker/24h?symbol={item_id}"
    data = {}
    r = requests.get(url, data=data)
    return {"status": 200,"msg": r.text}

#coinex 实时波动分析
@app.get("/coinex/volatility/{item_id}")
def read_root(item_id: str):
    url = f"https://www.coinex.com/res/quotes/asset/volatility/{item_id}"
    data = {}
    r = requests.get(url, data=data)
    return {"status": 200,"msg": r.text}

#okx 实时价格
@app.get("/okx/price/{item_id}")
def read_root(item_id: str):
    url = f"https://www.okx.com/priapi/v5/rubik/public/one-ticker?ccy={item_id}&t=1693450272414"
    data = {}
    r = requests.get(url, data=data)
    return {"status": 200,"msg": r.text}



#请求鱼池矿机数据
@app.get("/lbc/{token}")
def read_root(token:  None):

    ##########################################登录#########################################################
    if token is None:
        data = {
            'account': '86.15370406510',
            'password': 'a123456789'
        }

        headers = {'Content-Type': 'application/json'}

        res = requests.post(url='https://www.dxpool.com/api/v2/users/login', headers=headers, data=json.dumps(data))
        res_value = json.loads(res.text)
        token = res_value['token']

    try:
        ##########################################请求lbc旷工列表#########################################################
        data = {
        }

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            # 'Cookie': '_ga_XTG5DEQWQM=deleted; _ga_3BTDE2KT80=GS1.2.1690421988.1.0.1690421988.0.0.0; _ga=GA1.2.1678147956.1686722153; _gid=GA1.2.1875331741.1692170634; userID=5771; _csrf=94dc5551DgPePAE5zPYmtHaq2UN2x5prCK9UZveob7496e29466caf452dedc0f3a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%224OCQDAPjw8XshB6iNsm8PUIvYERFfWnM%22%3B%7D; _gat_UA-128180639-2=1; _ga_XTG5DEQWQM=GS1.1.1692170633.19.1.1692172003.0.0.0',
            'authorization': 'Bearer ' + token,
        }

        res = requests.get(
            url='https://www.dxpool.com/api/pools/lbc/accounts/6783/miners?group_id=7679&status=0&page_size=20&offset=0',
            headers=headers, data=data)

        return {"status": 200, "msg": res.text, "token": token}
    except Exception as e:
        return {"status": 201, "msg": str(e)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
