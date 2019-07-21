from account import Account
from studentAccount import StudentAccount
from businessAccount import BusinessAccount
from personalAccount import PersonalAccount

class Menu:

    def __init__(self, acc):
        self.acc = acc
      
    def start_menu(self):

        choice = 0

        while choice != "4":
            print('Option 1: withdraw')
            print('option 2: deposit')
            print('option 3: display balance')
            print('option 4: Exit')

            choice = input("Please choose an option : ")

            if choice == '1':
                amount = input("How much?: ")
                self.acc.withdraw(int(amount))
                
            if choice == '2':
                amount = input("How much?: ")
                self.acc.deposit(int(amount))
            
            if choice == "3":
                self.acc.showBalance()