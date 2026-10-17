class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d1 = Dog()
d1.bark()
d1.eat()   