class Account:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = 0
        self.overdraft = 0
        
#functions for transactios

    def showBalance(self):
        balance = self.balance
        print(f"balance is : {balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Sorry Insifficent Funds")
        else:
            self.balance -= amount