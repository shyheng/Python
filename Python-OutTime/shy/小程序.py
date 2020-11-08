#异常
try:
    age = int(input("age: "))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("对了")
except ValueError:#异常，处理错误报错
    print('出现了')







#def 构造方法

class Shy:#第一个字母大写，叫帕斯卡命名
    def __init__(self,x,y):#构造器 this
        self.x = x#java中的this
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

# 创建对象
# zph = Shy()
# zph.x = 10#赋值
# zph.y = 20
# print(zph.x)
# zph.draw()

#构造函数
shy = Shy(10,20)#以上数据存在x冲突
print(shy.x)






