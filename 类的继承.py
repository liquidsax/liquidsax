class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
        
dog = Dog("Fido")
cat = Cat("Mittens")

print(dog.name)   # 输出 "Fido"
print(dog.speak())   # 输出 "Woof!"
print(cat.name)   # 输出 "Mittens"
print(cat.speak())   # 输出 "Meow!"
