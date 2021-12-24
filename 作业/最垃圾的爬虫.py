from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

with open("mybaidu.html",mode="w",encoding="utf8") as f: #创建文件
    f.write(resp.read().decode("utf-8"))                 #保存在文件中
print("okk!")