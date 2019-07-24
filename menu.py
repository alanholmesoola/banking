from account import Account
from studentAccount import StudentAccount
from businessAccount import BusinessAccount
from personalAccount import PersonalAccount


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
                    print(amount)
                except ValueError:
                    print('\n Please enter a number\n')
                else:
                        self.acc.withdraw(int(amount))
            # deposit
            if choice == '2':
                try:
                    amount = int(input("How much?: "))
                except ValueError:
                    print('\n Please enter a number\n')
                else:
                    self.acc.deposit(int(amount))

            if choice == "3":
                self.acc.showBalance()
