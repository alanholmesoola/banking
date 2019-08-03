from app.menu import Menu
from app.accountBuilder import AccountBuilder
from app.database import AccountDatabase


try:
    name = (input("Please provide account name: "))
    accountList = AccountDatabase()
    currentAccount = accountList.load_account_by_account_name(name)
except Exception:
    print('\n Not an account\n')
else:
    ui = Menu(currentAccount)
    ui.start_menu()

# write to json on exit
accountList.save_account_by_account_name(name, currentAccount.balance)
