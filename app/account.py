class Account:

    def __init__(self, name, age, balance=0):
        self.name = name
        self.age = age
        self.balance = balance
        self.overdraft = 0

# functions for transactios

    def showBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        withdrawString = ""
        if self.balance < amount:
            withdrawString = "Sorry insufficent funds"
        else:
            self.balance -= amount
            withdrawString = f"Balance is: {self.balance}"
        return withdrawString
