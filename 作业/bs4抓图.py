#拿到主页面的源代码，然后提取到子页面的链接地址，herf
#通过herf拿到子页面的内容，从子页面找到图片的下载地址
#下载图片
import requests
from bs4 import BeautifulSoup
import time

url = "https://desk.zol.com.cn/"
resp = requests.get(url)
#把源代码交给bs

main_page = BeautifulSoup(resp.text,"html.parser")
list1 = main_page.find("ul",attrs={"class":"pic-list2 clearfix"}).find_all("li")
for a in list1:
    href = a.get("href")  #直接通过get就可以拿到属性的值
    #拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_text = child_page_resp.text
    #从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text,"html.parser")
    p = child_page.find("dd",attrs={"id":"tagfbl"})
    a = p.find("a")
    href_end = a.get("href")
    #下载图片
    href_resp = requests.get(href_end)
    href_resp.content      #这里拿到的是字节
    href_name = href_end.split("/")[-1]   #拿到url中的最后一个/以后的内容
    with open("href/"+href_name,mode="wb") as f:    #"href/"+表示将生成的文件加到href这个文件夹中
        f.write(href_resp.content)   #将图片内容写入到文件
    print("over!!!",href_name)
    time.sleep(1)    #一秒后继续请求，防止请求频率过快被服务器干掉

print("all over!!!")



