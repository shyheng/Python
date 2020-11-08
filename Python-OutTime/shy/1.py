# != 不等于
命令 = ""
出发 = False
while True:
    命令 = input(">").lower()
    if 命令 == "开始":
        if 出发:
            print("滚")
        else:
            出发 = True
        print("准备停车")
    elif 命令 == "stop":
        if not 出发:
            print("大哥，车已经停sb")
        else:
            出发 = False
        print("停了")
    elif 命令 == "help":
        print("""      # 保持装换
    开始- 开始停车
    stop- 为了停车
    quit- 老子不玩了
    """)
    elif 命令 == "quit":
        break#直到输入  quit结束
    else:
         print("老子不玩了")



