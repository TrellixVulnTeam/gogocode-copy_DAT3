class Order():
    def run(self,order_name):
        if order_name == "你好":
            print("给爷爬！")
        else:
            keyword = order_name[0:2]
            orderword = order_name[2:]
            if keyword == "打开":
                self.start_order(order_name)
            elif keyword == "退出" & "关闭":
                self.stop_order(order_name)

    def start_order(self,order_name):
        file = self.get_order(order_name)
        if file != None:
            win32api.ShellExecute(hwnd,op,file,params,dir,bShow)
            self.tell("正在打开" + order_name)
        else:
            sell.tell("没有找到对应指令")
     
    def get_order(self,name):
        with open("order.txt",mode="r+",encoding="utf-8") as f:
            data = f.readlines()
        for key,value in enumerate(data):
            result = value.split("路径为-->")#split将"路径为-->"左右两边分开放在列表里，左边为第一位，右边为第二位
            try:
                response = dict()  #赋值了一个空字典
                response["order_name"] = result[0].replace("\n"," ").strip()#键值对类型
                if name == response["order_name"]:
                    response["order_path"] = result[1].replace("\n"," ").strip()
                    response["exe_name"] = response["order_path"]
                    return response[return_data]

def tell(self,data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()