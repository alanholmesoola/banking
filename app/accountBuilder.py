from app.studentAccount import StudentAccount
from app.businessAccount import BusinessAccount
from app.personalAccount import PersonalAccount


class AccountBuilder:
    def build(self, acc_type, name, age, balance=0):
        # create instance of account class
        if acc_type == 'personal':
            return PersonalAccount(name, age, balance)

        if acc_type == "business":
            return BusinessAccount(name, age, balance)

        if acc_type == "student":
            return StudentAccount(name, age, balance)
