from account import Account
from studentAccount import StudentAccount
from businessAccount import BusinessAccount
from personalAccount import PersonalAccount


#create
#Each field type asks for input

#Account created

#display options (deposit - withdraw - view balance)

inputs = {
    'name' : "",
    'age' : "",
    'acc_type' : 0
}

for key, value in inputs.items():
    inputs[key] = input(f"please provide {key}: ")


#create instance of account class
acc = None

if inputs['acc_type'] == 'personal':
    acc = PersonalAccount(inputs['name'],inputs["age"])


if inputs['acc_type'] == "business":
    acc = BusinessAccount(inputs['name'],inputs["age"])


if inputs['acc_type'] == "student":
    acc = StudentAccount(inputs['name'],inputs["age"])



print('Option 1: withdraw')
print('option 2: deposit')
print('option 3: display balance')
choice = input("Please choose an option : ")


#account type based off the key value for acc_type