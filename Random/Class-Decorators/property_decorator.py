class Object:
    @property
    def sum(self):
        a = 1
        b = 2
        return f"The value is: {a+b}"


obj1 = Object()
print(obj1.sum)
