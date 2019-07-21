from studentAccount import StudentAccount
from businessAccount import BusinessAccount
from personalAccount import PersonalAccount

class AccountBuilder:
    def build(self, acc_type, name, age):
        #create instance of account class
        if acc_type == 'personal':
            return PersonalAccount(name, age)

        if acc_type == "business":
            return BusinessAccount(name, age)

        if acc_type == "student":
            return StudentAccount(name, age)
