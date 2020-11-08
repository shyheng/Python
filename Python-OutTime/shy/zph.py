is_hot = False#假的过，真的走。两个假的，执行最后一个
is_cold = False#

if is_hot:
    print("多喝水")
    print('shy')
elif is_cold:
    print("多穿衣服")
    print("zhp")
else:
    print("今天很美好")

print("dui")#一直执行




price = 10000
has_good_credit = True

if has_good_credit:
    down_paymet = 0.1 * price
else:
    down_paymet = 0.2 * price
print(f"Down payment: ${down_paymet}")


has_high_incom = True
has_good_credit = True
if has_high_incom and has_good_credit:
    print("shy")#逻辑运算符and，or，not

has_good_credit = True
shy = True
if has_good_credit and not shy:
    print("zph")



wen = 30#赋值语句
if wen > 30 :
    print("很热")
else:
    print("不热")



name = "jsdfadfs"
if len(name)<3:
    print("gun")
elif len(name) >50:
    print("hao")
else:
    print("hhhhhhh")




tizhong =int(input("体重多少: "))
unit  = input("告诉我是英镑（l）还是千克（k）: ")
if unit.upper() == "L":
    shy =  tizhong * 0.45
    print(f"你的体重是{shy}千克")
else:
    shy = tizhong / 0.45
    print(f"你的体重是{shy}磅")



# while循环
i = 1
while i <= 5 :
    print('*' * i)
    i = i + 1
print("Done")





