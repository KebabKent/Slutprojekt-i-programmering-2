import requests



""" Klasser för anställda """
class Employee:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Admin(Employee):
    def __init__(self, name, password, proffesion):
        super().__init__(name, password)
        self.proffesion = proffesion

class User(Employee):
    def __init__(self, name, password, proffesion):
        super().__init__(name, password)
        self.proffesion = proffesion



""" Klasser för att sortera djuren """
class Animal:
    def __init__(self, name, family, genus):
        self.name = name
        self.family = family
        self.genus = genus

class Fish(Animal):
    def __init__(self, name, family, genus, count):
        super().__init__(name, family, genus)
        self.count = count
        
class Amphibian(Animal):
   def __init__(self, name, family, genus, count):
        super().__init__(name, family, genus)
        self.count = count

class Reptile(Animal):
   def __init__(self, name, family, genus, count):
        super().__init__(name, family, genus)
        self.count = count

class Bird(Animal):
    def __init__(self, name, family, genus, count):
        super().__init__(name, family, genus)
        self.count = count

class Mammal(Animal):
   def __init__(self, name, family, genus, count):
        super().__init__(name, family, genus)
        self.count = count
print('din mamma')



def program_loop():
    print('din mamma ligger på pizza')



def get_num():
    x = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5')
    gg = x.json()
    print(gg)



if __name__ == '__main__':
    """ 
    Här ska de anställda hämtas in från excell filen med hjälp av 
    pythons excell bibliotek. En klass användare per anställd.
    """
    program_loop()
    get_num()







