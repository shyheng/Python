for shy in "alinfosif":
    print(shy)

for shy in ["shy","slfs","zph ","siri"]:
    print(shy)#换行

#range函数,
for shy in range(122):
    print(shy)#从0到121

for shy in range(5,50):
    print(shy)#5到49，数学中的[5,50)

for shy in range(5,50,20):
    print(shy)
    # 左开右闭


shy = [10,20,30]
zph = 0
for pyc in shy:
    zph += pyc
print(f"加起来：{zph}")

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")


shy = [5,65,56,5,99]
for x in shy:
    print("x" * x)

shy = [5,2,5,5]
for x_count in shy:
    output = ''
    for count in range(x_count):
        output += 'x'
        print(output)


name = ['ss','sd','dd','df']
print(name[2:4])#2，第三个；-2是第四个；  2:三个以后的数  2：4是dd df
name[0] = 'll'
print(name)#更改第一个


shu = [3,4,6,2,8,10]
max = shu[0]
for zu in shu:
    if zu > max:
        max = zu
print(max)


