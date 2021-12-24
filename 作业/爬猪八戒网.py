# 拿到页面源代码
# 提取和解析数据
import requests
from lxml import etree


url = "https://chongqing.zbj.com/search/f/?kw=网站建设"
resp = requests.get(url)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
for div in divs:    # 每一个服务商的div
    price = div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip("¥")  # [0]表示将内容拿出来放到列表里，这样就只会显示内容了
    
    title = "网站建设".join(div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))

    com_name = div.xpath('./div/div/a[1]/div[1]/p/text()')
    del com_name[0]  # 列表第一元素无用信息，去掉
    com_name = ' '.join(str(i) for i in com_name)    # 去掉列表的 [] 和 ‘’
    
    location = div.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]

    print(price)
    print(title)
    print(com_name)
    print(location)
