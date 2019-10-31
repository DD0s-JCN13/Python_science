class Animal:
    def __init__(self, name):
        self.name = name
    def jumper(self):
        print("Hop!")
    def runner(self):
        print("Don,Don,Don")
class Cat(Animal):
    def roar(self):
        print("Meow!")
class Dog(Animal):
    def roar(self):
        print("Woof!")
print(Animal.__dict__)
my_dog = Dog("tenzou")
my_cat = Cat("Madanna")
print(my_dog.name)
my_dog.roar()
my_dog.runner()
print(my_cat.name)
my_cat.roar()
my_cat.jumper()
