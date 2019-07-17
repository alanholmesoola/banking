from account import Account


class BusinessAccount(Account):

    def __init__(self, name, age):
        super(BusinessAccount, self).__init__(name, age)
        self.overdraft = 1000
        
        
        
    