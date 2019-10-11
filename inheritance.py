class Mammal:

    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


perro = Dog()
perro.walk()
