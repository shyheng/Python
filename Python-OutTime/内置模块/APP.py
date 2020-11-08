#随机值
import random
for i in range(3):
    print(random.random())

#随机值
import random
for i in range(3):
    print(random.randint(10,20))

#随机取值
import random
mam = ['ss', 'zph', 'xsx', 'sss']
shy = random.choice(mam)
print(shy)


#随机方法函数
import random
class Shy:
    def shy(self): #self和this一样
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
dice = Shy()
print(dice.shy())
