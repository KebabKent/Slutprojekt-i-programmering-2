import requests
import openpyxl
from getpwd import getpwd



""" Klasser för anställda """
class Employee:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        """ Här ska alla metoder som båda klasserna har gemensamma vara """


class Admin(Employee):
    def __init__(self, name, password):
        super().__init__(name, password)
        # Ärv metoder som admin ska komma åt

class User(Employee):
    def __init__(self, name, password, proffesion):
        super().__init__(name, password)
        self.proffesion = proffesion
        # Ärv metoder som user ska komma åt



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



def login():
    path = "C:/Users/nikodemus.nilssonoh/Documents/Programmering/Github/Slutprojekt-i-programmering-2/Employees.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_ro = sheet_obj.max_row

    anv_nam = str(input('Username: '))

    for x in range(1, max_ro + 1):
        for i in range(3):
            anv = sheet_obj.cell(row = x, column = 1)

            if anv.value == anv_nam:
                password = getpwd() #Frågar om lösenord och gör så att man inte ser vad som skrivs in
                print(password)
                pass_check = sheet_obj.cell(row = x, column = 3)

                if password == pass_check.value:
                    print('Du hade rätt lösenord')

                    """ Gör ett klass objekt av användaren """

                    role = sheet_obj.cell(row = x, column = 5)

                    if role.value == 'User':
                        print('User')
                        profession = sheet_obj.cell(row = x, column = 6)
                        logged_in_user = User(anv_nam, pass_check.value, profession.value)  
                        
                        print(logged_in_user.proffesion, logged_in_user.password)
                    

                    elif role.value == 'Admin':
                        print('Admin')
                        logged_in_user = Admin(anv_nam, pass_check.value)


                    break



def program_loop():
    print('din mamma ligger på pizza')



def get_num():
    x = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=1')
    gg = x.json()
    print(gg[0])



if __name__ == '__main__':
    """ 
    Här ska de anställda hämtas in från excell filen med hjälp av 
    pythons excell bibliotek. En klass användare per anställd.
    """
    login()
    program_loop()
    get_num()






