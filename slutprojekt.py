import requests
import openpyxl
from getpwd import getpwd



""" Klasser för anställda """
class Bank:
    def __init__(self, name, password, proffession):
        self.name = name
        self.__password = password
        self.proffession = proffession
        """ Här ska alla metoder som båda klasserna har gemensamma vara """
    
    def return_password(self):
        return self.__password


class Admin(Bank):
    def __init__(self, name, password, proffession):
        super().__init__(name, password, proffession)
        # Ärv metoder som admin ska komma åt

class User(Bank):
    def __init__(self, name, password, proffession):
        super().__init__(name, password, proffession)
        # Ärv metoder som user ska komma åt

class Underage_user(Bank):
    def __init__(self,name, password, proffession):
        super().__init__(name, password, proffession)



def login():
    path = "C:/Users/nikodemus.nilssonoh/Documents/Programmering/Github/Slutprojekt-i-programmering-2/Employees.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_ro = sheet_obj.max_row

    anv_nam = str(input('Username: '))

    for x in range(1, max_ro + 1):
        anv = sheet_obj.cell(row = x, column = 1)

        if anv.value == anv_nam:
            password = getpwd() #Frågar om lösenord och gör så att man inte ser vad som skrivs in
            print(password) # Göra så att man kan välja att se lösenordet innan man skriver in det
            pass_check = sheet_obj.cell(row = x, column = 3)

            if password == pass_check.value:
                print('Du hade rätt lösenord')

                """ Gör ett klass objekt av användaren """

                role = sheet_obj.cell(row = x, column = 5)
                profession = sheet_obj.cell(row = x, column = 6)
                
                if role.value == 'User':
                    print('User')
                    logged_in_user = User(anv_nam, pass_check.value, profession.value)
                    print(logged_in_user.proffession, logged_in_user.return_password())
                    return logged_in_user
                
                elif role.value == 'Underage_user':
                    print('Underage_user')
                    logged_in_user = Underage_user(anv_nam, pass_check.value, profession.value)
                    print(logged_in_user.proffession, logged_in_user.return_password())
                    return logged_in_user

                elif role.value == 'Admin':
                    print('Admin')
                    logged_in_user = Admin(anv_nam, pass_check.value, profession.value)
                    return logged_in_user

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






