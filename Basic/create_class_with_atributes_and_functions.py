
class Dog:
    def __init__(self, name: str):
        self.name = name

    def makeSound(self):
        return 'Auau'


d1 = Dog('teste')
print(d1.name)
print(d1.makeSound())
