from account import Account


class PersonalAccount(Account):

    def __init__(self, name, age):
        super(PersonalAccount, self).__init__(name, age)
        self.overdraft = 200
