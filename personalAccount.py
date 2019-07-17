from account import Account


class PersonalAccount(Account):

    def __init__(self, name, age):
        self.overdraft = 200
        super(PersonalAccount, self).__init__(name, age)
        
        
    