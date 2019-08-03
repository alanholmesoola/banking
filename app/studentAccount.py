from app.account import Account


class StudentAccount(Account):

    def __init__(self, name, age, balance):
        super(StudentAccount, self).__init__(name, age, balance)
        self.overdraft = 0
