from menu import Menu
from accountBuilder import AccountBuilder

#display options (deposit - withdraw - view balance)

# Get User Input
inputs = {
    'name' : "",
    'age' : "",
    'acc_type' : 0
}

for key, value in inputs.items():
    inputs[key] = input(f"please provide {key}: ")

# Build Account
acc_builder = AccountBuilder() 
acc = acc_builder.build(inputs['acc_type'], inputs['name'], inputs['age'])

# Disaplay UI
ui = Menu(acc)
ui.start_menu()
