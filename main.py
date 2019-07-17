#create
#Each field type asks for input

#Account created

#display options (deposit - withdraw - view balance)

inputs = {
    'name' : "",
    'age' : "",
    'acc_type' : ""
}

for key, value in inputs.items():
    inputs[key] = input(f"please provide {key}: ")


#create instance of account class

#account type based off the key value for acc_type