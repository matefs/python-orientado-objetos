
class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    pass


a1 = Animal('asd')
print(a1.name)

c1 = Cat('asd')
print(c1.name)
