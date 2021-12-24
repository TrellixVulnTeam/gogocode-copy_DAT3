import re

#findall：匹配字符串中所有符合正则的内容
lst = re.findall(r"\d+","我的电话号码是:10086,他的电话号码是10010")#r是为了防止转义,vscode中不加也行
print(lst)

#finditer：匹配字符串中所有的内容（返回的是迭代器），从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+","我的电话号码是:10086,他的电话号码是10010")
print(it)
for i in it:
    print(i.group())

#迭代器效率比列表高，所以一般都用迭代器

s = re.search(r"\d+","我的电话号码是:10086,他的电话号码是10010")
print(s.group())
#search，找到一个结果就返回，返回的结果是match对象，拿数据需要.group()


m = re.match(r"\d+","10086,他的电话号码是10010")
print(m.group())
#match从头开始匹配,等同于 r"^\d+" 而search是从全文匹配，



#预加载正则表达式
obj = re.compile(r"\d+")#好处：可以反复用，尤其是正则表达式较长时可以节省输入时间
ret = obj.finditer("我的电话号码是:10086,他的电话号码是10010")
for it in ret:
    print(it.group())

shuju = """
1是a,2是b,3是c,
4是d,5是e,6是f,
7是g,8是h,9是i,
"""
obj = re.compile(r"(?P<序号>.)是(?P<字母>.*?),",re.S)
#其中re.S能让.匹配换行符,vscode中不添加也能匹配换行
#(?P<名字>正则)是指把'正则获得的内容'存进'名字'的组里，通过group("名字")来打印特定内容
result = obj.finditer(shuju)
for it in result:
    print(it.group("序号"))
    print(it.group("字母"))