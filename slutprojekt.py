import requests
import openpyxl
from getpwd import getpwd
import time



""" Klasser för anställda """
class Bank:
    def __init__(self, name, password, proffession, row):
        self.name = name
        self.__password = password
        self.proffession = proffession
        self.row = row
        """ Här ska alla metoder som båda klasserna har gemensamma vara """
    
    def return_password(self):
        return self.__password
    
    def return_row(self):
        return self.row

class Admin(Bank):
    def __init__(self, name, password, proffession, row):
        super().__init__(name, password, proffession, row)
        # Ärv metoder som admin ska komma åt
    
    def shange_password(self):
        pass

    def shange_user_password():
        pass

class User(Bank):
    def __init__(self, name, password, proffession, row):
        super().__init__(name, password, proffession, row)
        # Ärv metoder som user ska komma åt
    
    def shange_password(self):
        pass

    def check_account_balance(self):
        pass

class Underage_user(Bank):
    def __init__(self,name, password, proffession, row):
        super().__init__(name, password, proffession, row)

    def check_account_balance(self):
        pass



def login():
    path = "C:/Users/nikodemus.nilssonoh/Documents/Programmering/Github/Slutprojekt-i-programmering-2/Employees.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_ro = sheet_obj.max_row

    """ Kollar om användaren finns och vart den finns"""
    print('\n<--Logga in-->')
    for i in range(3):
        anv_nam = str(input('Username: '))

        for xx in range(1, max_ro +1):
            anv = sheet_obj.cell(row = xx, column = 1)
            if anv.value == anv_nam:
                print('Användaren finns\n')
                time.sleep(0.5)
                break
        
        if anv.value == anv_nam:
            break

        else:
            print('\nAnvändaren finns inte försök igen\n')
            time.sleep(0.5)

    """ Tar lösenordet och loggar in användaren med användarnamnet """
    if anv.value == anv_nam:
        for ii in range(3):
            anv = sheet_obj.cell(row = xx, column = 1)

            if anv.value == anv_nam:
                password = getpwd() #Frågar om lösenord och gör så att man inte ser vad som skrivs in
                print(password) # Göra så att man kan välja att se lösenordet innan man skriver in det
                pass_check = sheet_obj.cell(row = xx, column = 3)

                if password == pass_check.value:
                    print('Du hade rätt lösenord')

                    """ Gör ett klass objekt av användaren """

                    role = sheet_obj.cell(row = xx, column = 5)
                    profession = sheet_obj.cell(row = xx, column = 6)
                    row = xx
                    
                    if role.value == 'User':
                        print('In loggad som User')
                        logged_in_user = User(anv_nam, pass_check.value, profession.value, row)
                        #print(logged_in_user.proffession, logged_in_user.return_password())
                        return logged_in_user
                    
                    elif role.value == 'Underage_user':
                        print('In loggad som Underage_user')
                        logged_in_user = Underage_user(anv_nam, pass_check.value, profession.value, row)
                        #print(logged_in_user.proffession, logged_in_user.return_password())
                        return logged_in_user

                    elif role.value == 'Admin':
                        print('In loggad som Admin')
                        logged_in_user = Admin(anv_nam, pass_check.value, profession.value, row)
                        return logged_in_user
                    break



def skapa_ny_anvandare():
    """ Här ska programmet göra en ny användare genom att lägga in användaren i excell dokumentet"""
    print('gay shit (bokstavligt talat)')
    time.sleep(0.5)
    pass
    


def program_loop(user):
    while True:
        move_ans = int(input('\n<------------Vad vill du göra?------------>' + 
                        '\ngreg 1 (1)' + 
                        '\ngrej 2 (2)' + 
                        '\nLogga ut (3)' + 
                        '\nSvar: '))
        if move_ans == 1:
            break

        elif move_ans == 2:
            break

        elif move_ans == 3:
            break

        else:
            print('Ditt svar är inte giltigt försök igen!')



def get_num():
    x = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=1')
    gg = x.json()
    print(gg[0])



if __name__ == '__main__':
    """ 
    Här ska de anställda hämtas in från excell filen med hjälp av 
    pythons excell bibliotek. En klass användare per anställd.
    """
    while True:
        log_not = int(input('\n<------------Huvudmeny------------>'+
                        '\nLogga in (1)' +
                        '\nSkapa ny användare (2)' 
                        '\nAvsluta programm (3)' + 
                        '\nSvar: '))

        if log_not == 1:
            user = login()
            program_loop(user)
            #get_num()
            print('Ligger på rad: ', user.return_row(), ' i excel dokumentet.')
        
        elif log_not == 2:
            skapa_ny_anvandare()
        
        elif log_not == 3:
            print('Hej då!')
            break

        else:
            print('Ditt svar är inte tillgängligt var god försök igen!')

        
       
