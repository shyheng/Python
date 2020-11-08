class Shy:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"我是{self.name}")


john = Shy("shao")
john.talk()
# java中创建对象为shy s = new shy（）;
bob = Shy("zhang")
bob.talk() 
