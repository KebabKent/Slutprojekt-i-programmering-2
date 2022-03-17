import requests

x = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5')
gg = x.json()
print(gg)


class Employee:
    def __init__(self, name, proffesion):
        self.name = name
        self.proffesion = proffesion


class Admin:
    def __init__(self, name, proffesion, password):
        super().__init__(name, proffesion)
        self.password = password


class Animal:
    def __init__(self, name):
        self.name = name


class Fish(Animal):
    def __init__(self, name, family, genus):
        super().__init__(name)
        self.family = family
        self.genus = genus

class Amphibian(Animal):
    pass

class Reptile(Animal):
    pass

class Bird(Animal):
    pass

class Mammal(Animal):
    pass


