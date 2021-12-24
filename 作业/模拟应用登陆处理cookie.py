# 登录-》得到cookie
# 带着cookie去请求到书架url -》 书架上的内容

# 必须得把上面两个操作连起来
# 我们可以用session（汉语翻译为会话）进行请求，session可以认为是一连串的请求，并且在这个过程cookie不会丢失
import requests


session = requests.session()
data = {
    "username" : "18256731893",
    "password" : "zjl5951357"
}

# 伪造成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30 ",
    "cookie" : "SMYUV=1633271576081349; SUV=1633271576080286; UM_distinctid=17c469276142e6-0480a37ab46be8-513c164a-190140-17c469276158da; guest_uid=guest_435116763; source=10000_; newgift_state=1; ppinf=5|1636181829|1637391429|dHJ1c3Q6MToxfGNsaWVudGlkOjU6MTAwMjZ8dW5pcW5hbWU6MjY6JUU3JTk0JUE4JUU2JTg4JUI3NTM4NDU3ODJ8Y3J0OjEwOjE2MzYxODE4Mjl8cmVmbmljazowOnx1c2VyaWQ6NDI6ZWdpb2dxeGZncmplaTV6bGwzYzJ0NHhrcXlqa2dvcnhAc29nb3UuY29tfA; pprdig=baVVMMsKtcN6lJdka-UP-pVWwNJ2NnnWhoEHvEVfJ7Q9uJU9ceYhFA_1JFK5oqS4UFjNe-yMokPf5Uh8CjBDzSwETBi4mj5eetJDvS7t_04VKjGOrc0pIfdrB84_Kx7G807UFrFigy22dfFOnow77-flwbuFcaAlEgDhjGMgHSM; ppinfo=4f4602abfb; passport=5|1636181829|1637391429|dHJ1c3Q6MToxfGNsaWVudGlkOjU6MTAwMjZ8dW5pcW5hbWU6MjY6JUU3JTk0JUE4JUU2JTg4JUI3NTM4NDU3ODJ8Y3J0OjEwOjE2MzYxODE4Mjl8cmVmbmljazowOnx1c2VyaWQ6NDI6ZWdpb2dxeGZncmplaTV6bGwzYzJ0NHhrcXlqa2dvcnhAc29nb3UuY29tfA|6d333c3abb|baVVMMsKtcN6lJdka-UP-pVWwNJ2NnnWhoEHvEVfJ7Q9uJU9ceYhFA_1JFK5oqS4UFjNe-yMokPf5Uh8CjBDzSwETBi4mj5eetJDvS7t_04VKjGOrc0pIfdrB84_Kx7G807UFrFigy22dfFOnow77-flwbuFcaAlEgDhjGMgHSM; sgid=20-52721975-AWGGJ0VicLSMDlzLiaWVR5LzQ; ppmdig=16361816160000004c013e0285ec177346cfe3667a86fc1d; reader_help_tip=1; QIDIANID=sfb91xrAwcYSGArTbT1kYYWqq5Gw8h/i71IkZchtC3c="
}

# 登录
url = "https://account.sogou.com/web/login"
session.post(url, data=data, headers=headers)

# 那书架上的数据
# 刚才的session中是有cookie的
resp = session.get("https://xs.sogou.com/api/pc/v1/user/info", headers=headers)
resp1 = session.get("https://xs.sogou.com/html/web/api/forcebreak.json", headers=headers) 

print(resp.json())
print(resp1.json())

