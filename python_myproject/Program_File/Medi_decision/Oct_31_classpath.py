class Cat:
    def __init__(self, name):
        self.name = name
    def roar(self):
        print("Meow!")
class Dog:
    def __init__(self, name):
        self.name = name
    def roar(self):
        print("Woof!")
the_cat_1 = Cat("Lily")
the_dog_1 = Dog("Mendora")
the_cat_1.roar()
the_dog_1.roar()