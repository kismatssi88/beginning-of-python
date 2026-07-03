class employee:
    def __init__(self,name,id ,age):
        self.name = name
        self.id = id
        self.age = age
        
    def nameage(self):
        return '{} {}'.format(self.name, self.age)


e1 = employee("kessi", 8848, 20)
e2= employee("messi", 6969, 39)
print(e1.name)
print(e2.age)
print(e1.id)
print(e1.nameage())