# 猜字谜3次机会
shy = 9
zph = 0
pcy = 3
while zph < pcy :       #选中变量shift+F6，重命名变量
    cai = int(input("猜"))
    zph += 1
    if cai == shy:
        print("真他m聪明")
        break#没有就循环3次，猜正确就停止，
else:
    print("我给你3次机会，你傻逼吧")
