from app.account import Account
from app.studentAccount import StudentAccount
from app.businessAccount import BusinessAccount
from app.personalAccount import PersonalAccount
from app.database import AccountDatabase


class Menu:

    def __init__(self, acc):
        self.acc = acc

    def start_menu(self):

        choice = 0

        # while loop for menu dispay
        while choice != "4":
            print('\nOption 1: withdraw')
            print('option 2: deposit')
            print('option 3: display balance')
            print('option 4: Exit\n')

            choice = input("Please choose an option : ")

            # menu choice with value error catch
            if choice == '1':
                # Withdraw
                try:
                    amount = int(input("How much?: "))
                except ValueError:
                    print('\n Please enter a number\n')
                else:
                    withdrawString = self.acc.withdraw(int(amount))
                    print(withdrawString)
            # deposit
            if choice == '2':
                try:
                    amount = int(input("How much?: "))
                except ValueError:
                    print('\n Please enter a number\n')
                else:
                    self.acc.deposit(int(amount))

            if choice == '3':
                balance = self.acc.showBalance()
                print(f"\nBalance is : {balance}")
