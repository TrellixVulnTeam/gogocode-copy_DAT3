import requests

artist = input()
url = "https://music.163.com/#/search/m/?s=周杰伦&type=100"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
}

resp = requests.post(url,headers=headers)
print(resp.text)
resp.close()