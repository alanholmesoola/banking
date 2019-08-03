from app.account import Account


class PersonalAccount(Account):

    def __init__(self, name, age, balance):
        super(PersonalAccount, self).__init__(name, age, balance)
        self.overdraft = 200
