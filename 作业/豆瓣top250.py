# 拿到网页源代码   requests
# 通过re来提取想要的有效信息  re
import requests
import re
import csv  # 一种文件格式，用来储存数据

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30 "
}
resp = requests.get(url, headers=headers)
page_content = resp.text
# print(resp.text)
# 解析数据
# obj = re.compile(r'<img width="100" alt="(?P<name>.*?)".*?<span>(?P<评论>.*?)</span>')
obj = re.compile(r'<img width="100" alt="(?P<name>.*?)".*?<span>(?P<评论>.*?)</span>', re.S)
result = obj.finditer(page_content)
f = open("data.csv", mode="w", newline='')  # newline=''是为了解决数据导入后每行之间会产生空行的问题
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("评论"))
    dic = it.groupdict()
    csvwriter.writerow(dic.values())
f.close()  # 可能是为了防止一直创建？
print("over!")
