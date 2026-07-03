class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


# Create objects outside the class
s1 = Student("kessi", 67, 20)
s2 = Student("messi", 10, 39)

print(s1.id)
print(s2.name)