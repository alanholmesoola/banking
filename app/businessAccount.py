from app.account import Account


class BusinessAccount(Account):

    def __init__(self, name, age, balance):
        super(BusinessAccount, self).__init__(name, age, balance)
        self.overdraft = 1000
