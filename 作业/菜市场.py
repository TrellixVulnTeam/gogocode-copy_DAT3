# 使用bs4进行解析，拿到数据
import requests
from bs4 import BeautifulSoup
import csv

url = "https://nonghecj.com/"
resp = requests.get(url)

f = open("菜价.csv", mode="w", newline='')
csvwriter = csv.writer(f)

# 解析数据
# 把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # "html.parser"是为了指定html解析器，一般不写也不影响，会报警告然后自动分析
# 从bs对象中查找数据
# find(标签，属性=值)       找到第一个就返回
# find_all(标签，属性=值)   会把页面所有找到的返回
table = page.find("body")  # 若属性是python的关键字,则要在属性后面加下划线(_)
# 或者改用字典例如：table = page.find("div",attrs={"id":"__nuxt"})这样做好处可以避免属性是python关键字
# 拿到所有数据行
trs = table.find_all("tr")[1:]  # 做切片，从第2个（1）开始切，第1个（0）没用信息就没了
for tr in trs:  # 对每一行循环处理
    try:
        tds = tr.find_all("td")  # 拿到每行中的所有td
        num = tds[0].text.strip()
        name = tds[1].text.strip()  # .text表示拿到被标签标记的内容
        danwei = tds[2].text.strip()
        price = tds[3].text.strip()
        csvwriter.writerow([num, name, danwei, price])
    except:
        continue
f.close()
print("over")
