from account import Account


class StudentAccount(Account):

    def __init__(self, name, age):
        super(StudentAccount, self).__init__(name, age)
        self.overdraft = 0
        
        
        
    