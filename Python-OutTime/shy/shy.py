print("hello world")
prie = 10
print(prie)
# is_shy = False

# full_name = "shy"
# age = 20
# is_new = True


name =  input("what is your name")
print("hi"+name)


name =  input("what is your name？ ")
favorite_color = input("what is your favorit？ ")
print(name+"likes"+favorite_color)


birth_year = input("birth year: ")
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)

weight_lbs  = input("weight (lbs): ")
weight_lbs  = int(weight_lbs)*0.45
print(weight_lbs)

shy = "sljseifs sljfiwj lsj i"
print(shy[0:6])#索引从第一到7个
zph = shy[:]#全部
print(zph)
# len（）函数
shy = "sllsksasl"
print(len(shy))#多少字符
print(shy.upper())#全部大写
print(shy.lower())#全部小写
print(shy.find("s"))#查找s在哪，输入一整个，查找从第一个开始找
print(shy.replace("sks","abc"))#替换sks为abc
print("sll"in shy)#用布尔类型判断sll是否在shy中


x = 10
x = x + 3
x += 3
print(x)

x = 2.9
print(round(x))#整数化四舍五入3
print(abs(-2.9))#绝对值

import math
print(math.ceil(2.9))#向上取整3
print(math.floor(2.9))#向下取整2









