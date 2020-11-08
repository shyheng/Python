# 矩阵
shy = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
shy [0][1] = 20 #替换
print(shy[0][1])#2，索引

for row in shy:
    for item in row:
        print(item)

shy = [5,4,6,2,1]

shy.append(20)#增加一个数20在最后
print(shy)

shy.insert(0,10)
print(shy)#最前面增加一个数10

shy.remove(5)
print(shy)#移除一个数5

shy.pop()
print(shy)#移除最后一个数字20

print(shy.index(6))#索引6的位置2

print(20 in shy)#查找20是否在shy中出现布尔类型

print(shy.count(6))#查找6有几个

shy.sort()#排序
shy.reverse()#从大到小
print(shy)#这个方法不能在打印区运行

shy1 = shy.copy()#给shy1赋值

shy.clear()
print(shy)#清除所有

shy = [2,2,4,4,6,6,3,1]
zph = []
for shy1 in shy:
    if shy1 not in zph:
        zph.append(shy1)
print(zph)#清除相同元素

# shy = (1,2,3)
# shy[1] = 10
# print(shy[0])#输入错误，元组不可改变

#解压
shy = (1,2,3)#先锁,封装
# x = shy[0]
# y = shy[1]
# z = shy[2]
x,y,z = shy
print(y)

# 字典
shy = {
    'name' : 'js',
    'age' : 30,
    'zph' : True
}
shy ['name'] = "zph"
print(shy.get('sheng','2011 2 2'))
print(shy['name'])
shy['sheng'] = '2011 2 2'
print(shy['sheng'])#在上面读取不了sheng，能用get


# 阿拉伯数字换英语
shy = input("请输入数字")
zi = {
        '0':'zero',
        '1': 'One',
        '2' : 'two',
        '3' : 'three ',
        '4' : 'four ',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight ',
         '9' : 'nine',

}
output = ""
for ch in shy :
    output += zi.get(ch,'!') + ""
print(output)




