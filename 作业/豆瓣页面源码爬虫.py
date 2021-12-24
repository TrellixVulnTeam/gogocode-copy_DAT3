import requests
from requests.models import Response

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
param = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

# 伪造成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30 "
}

resp = requests.get(url=url, params=param, headers=headers)

print(resp.json())
resp.close()  # 关掉resp，否则多次使用会提示请求次数过多
