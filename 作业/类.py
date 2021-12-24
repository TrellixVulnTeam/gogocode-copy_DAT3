class Person:

    def __init__(self, name):
        self.name = name
        self.__samll_name = f'xiao{name}'

    # @property  # 装饰器
    # 通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。
    def small_name(self):  # 通过函数将私有变量返回出去
        return self.__samll_name

    # @small_name.setter  # 必须要用@property才能用，否则此时不是属性
    # def small_name(self, value):
    #    self.__samll_name = value


if __name__ == '__main__':
    p1 = Person('zhangsan')
    print(p1.name)
    # print(p1.__samll_name) # __small_name为私有变量，无法访问
    p1.name = 'lisi'
    print(p1.name)
    print(p1.small_name())
    # 通过调用函数访问私有变量

    # print(p1.small_name)
    # 通过使用@property将其作为属性调用不需要加()
