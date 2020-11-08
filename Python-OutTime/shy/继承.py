class Chong:
    def walk(self):
        print('walk')


class Dog(Chong):#继承
    pass



class Cat:
    def shy(self):
        print("瞎搞")

cat = Cat()
cat.shy()

dog = Dog()
dog.walk()






