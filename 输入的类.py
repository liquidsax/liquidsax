class Person:
    num = 1
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Sayhello(self):
        print("hello!")
    def PrintName(self):
        print("姓名: ",self.name)#告诉我姓名
    def PrintNum(self):
        print(Person.num)#告诉我人数
#主体
P1 = Person("包更",22)
P2 = Person("王杰",23)
#输出测试
P1.PrintName()
P2.PrintNum()
Person.num=2
P2.PrintNum()

        

        