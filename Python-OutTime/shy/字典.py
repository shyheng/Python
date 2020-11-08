# 添加表情
yong = input('>')
shy = yong.split(" ")
emojis = {
    ":)": "😊",#win+分号或者句号
    ":(" :"😒"
}
output = ""
for biao in shy:
    output += emojis.get(biao,biao) + " "
print(output)