import requests
import openpyxl
from getpwd import getpwd
import time



""" Klasser för anställda """
class Bank:
    def __init__(self, name, password, role, row):
        self.name = name
        self.__password = password
        self.role = role
        self.row = row
        """ Här ska alla metoder som alla klasserna har gemensamma vara """
    
    def return_password(self):
        return self.__password
    
    def return_row(self):
        return self.row
    
    def return_role(self):
        return self.role

class Admin(Bank):
    def __init__(self, name, password, role, row):
        super().__init__(name, password, role, row)
        # Ärv metoder som admin ska komma åt
    
    def shange_password(self):
        pass

    def check_user_balance():
        pass

class User(Bank):
    def __init__(self, name, password, role, row, balance):
        super().__init__(name, password, role, row)
        self.balance = balance
        # Ärv metoder som user ska komma åt
    
    def shange_password(self):
        pass

    def check_account_balance(self):
        return self.balance

class Underage_user(Bank):
    def __init__(self,name, password, role, row, balance):
        super().__init__(name, password, role, row)
        self.balance = balance

    def check_account_balance(self): # Ska bara kunna kolla hur myket pengar som finns.
        return self.balance



def login():
    path = "./Employees.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_ro = sheet_obj.max_row

    """ Kollar om användaren finns och vart den finns"""
    print('\n<--Logga in-->')
    for i in range(3):
        anv_nam = str(input('Förnamn: '))
        anv_eft_nam = str(input('Efternamn: '))

        for xx in range(1, max_ro +1):
            anv_n = sheet_obj.cell(row = xx, column = 1)
            anv_eft_n = sheet_obj.cell(row = xx, column = 2)

            if anv_n.value == anv_nam and anv_eft_n.value == anv_eft_nam:
                print('Användaren finns\n')
                time.sleep(0.5)

                """ Tar lösenordet och loggar in användaren med användarnamnet """
                for ii in range(3):
                    password = getpwd() #Frågar om lösenord och gör så att man inte ser vad som skrivs in
                    print(password) # Göra så att man kan välja att se lösenordet innan man skriver in det
                    pass_check = sheet_obj.cell(row = xx, column = 3)

                    if password == pass_check.value:
                        print('Du hade rätt lösenord')

                        """ Gör ett klass objekt av användaren """

                        role = sheet_obj.cell(row = xx, column = 5)
                        row = xx
                        
                        if role.value == 'User':
                            print('In loggad som User')
                            balance = sheet_obj.cell(row = xx, column = 4)
                            logged_in_user = User(anv_n, pass_check.value, role.value, row, int(balance.value))
                            #print(logged_in_user.role, logged_in_user.return_password())
                            return logged_in_user
                        
                        elif role.value == 'Underage_user':
                            print('In loggad som Underage_user')
                            balance = sheet_obj.cell(row = xx, column = 4)
                            logged_in_user = Underage_user(anv_n, pass_check.value, role.value, row, int(balance.value))
                            #print(logged_in_user.role, logged_in_user.return_password())
                            return logged_in_user

                        elif role.value == 'Admin':
                            print('In loggad som Admin')
                            logged_in_user = Admin(anv_n, pass_check.value, role.value, row)
                            return logged_in_user
                        break
                break
        
        if anv_n.value == anv_nam and anv_eft_n.value == anv_eft_nam:
            break
        
        elif i<2:
            print('\nAnvändaren finns inte försök igen!\n')
            time.sleep(0.5)

        else:
            print('\nAnvändaren finns inte!\n')
            time.sleep(0.5)



def skapa_ny_anvandare():
    """ Här ska programmet göra en ny användare genom att lägga in användaren i excell dokumentet"""
    print('gay shit (bokstavligt talat)')
    time.sleep(0.5)
    


def admin_loop(user):
    while True:
        try:
            move_ans = int(input('\n<------------Vad vill du göra?------------>' + 
                            '\nSkapa ny användare (1)' + 
                            '\ngrej 2 (2)' + 
                            '\nLogga ut (3)' + 
                            '\nSvar: '))

            if move_ans == 1:
                skapa_ny_anvandare()

            elif move_ans == 2:
                break

            elif move_ans == 3:
                break

        except:
            print('Ditt svar är inte giltigt försök igen!')



def user_loop(user):
    while True:
        try:
            move_ans = int(input('\n<------------Vad vill du göra?------------>' + 
                            '\nMoney money money money... MONEY!(I falsett) (1)' + 
                            '\ngrej 2 (2)' + 
                            '\nLogga ut (3)' + 
                            '\nSvar: '))

            if move_ans == 1:
                print('\nDet finns: ', user.check_account_balance(), ' svenska riksdaler på kontot.')
                time.sleep(0.5)

            elif move_ans == 2:
                break

            elif move_ans == 3:
                break

        except:
            print('Ditt svar är inte giltigt försök igen!')



def underage_user_loop(user):
    while True:
        try:
            move_ans = int(input('\n<------------Vad vill du göra?------------>' + 
                            '\nMoney money money money... MONEY!(I falsett) (1)' + 
                            '\nLogga ut (2)' + 
                            '\nSvar: '))

            if move_ans == 1:
                print('\nDet finns: ', user.check_account_balance(), ' svenska riksdaler på kontot.')
                time.sleep(0.5)

            elif move_ans == 2:
                break

        except:
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
        try:
            log_not = int(input('\n<------------Huvudmeny------------>'+
                            '\nLogga in (1)' +
                            '\nAvsluta programm (2)' + 
                            '\nSvar: '))

            if log_not == 1:
                user = login()

                if user.return_role() == 'User':
                    user_loop(user)
                
                elif user.return_role() == 'Underage_user':
                    underage_user_loop(user)

                elif user.return_role() == 'Admin':
                    admin_loop(user)

                #get_num()
                #print('Ligger på rad: ', user.return_row(), ' i excel dokumentet.')
            
            elif log_not == 2:
                print('Hej då!')
                break

        except:
            print('Ditt svar är inte tillgängligt var god försök igen!')
            time.sleep(3)



