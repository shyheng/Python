# 创造函数def
def shy(fan_name):
    print(f'hi{fan_name}')
    print('欢迎来到我的世界')

print('不知道')#先定义后调用,多重方法调用
shy("zph")
shy("pcy")
print('再见')



def shy (xing,ming):
    print(f'hi {xing},{ming}')
    print('欢迎来到我的世界')

print("不知道")
shy("zhang",'heng')
print('再见')

def shy(zph):
    print(zph * zph)#none
print(shy(3))

def shy(zph):
    return zph * zph
print(shy(55))


def emoji(yong):
    shy = yong.split(" ")
    emojis = {
        ":)": "😊",  # win+分号或者句号
        ":(": "😒"
    }
    output = ""
    for biao in shy:
        output += emojis.get(biao, biao) + " "
    return output
yong = input('>')

print(emoji(yong))

# java中的new，Python中的def
#
#
#
#
#
#
