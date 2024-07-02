# Abstraction
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal):

    def sound(self):
        return "Meow"


dog = Dog("Rancho")
print(dog.sound())

cat = Cat("CAT")
print(cat.sound())
