def ask(name="shy"):
    print(name)
class Pson:
    def __init__(self):
        print("bass")
#
def print_type(item):
    print(type(item))

def decorator_func():
    print("dec")
    return ask
my_ask = decorator_func()
my_ask('abs')
# 函数可以当返回值

# obj_list = []
# obj_list.append(ask)
# obj_list.append(Pson)
# for item in obj_list:
#     print(item())
#
#
#
# my_class = Pson
# my_class()
#
# my_fun = ask
# my_fun("shy")








