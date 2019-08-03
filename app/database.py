import json
from app.accountBuilder import AccountBuilder


class AccountDatabase():
    def __init__(self):
        self.path = 'app/database/accounts.json'
        self.builder = AccountBuilder()

    def load_account_by_account_name(self, account_name):
        all_accounts = self._read()

        for account in all_accounts['accounts']:
            if account['account_holder'].lower() == account_name.lower():
                account = self.builder.build(
                    account['account_type'],
                    account['account_holder'],
                    account['age'],
                    account['amount'])
                return account

        raise Exception('Account not found error')

    def save_account_by_account_name(self, account_name, balance):
        all_accounts = self._read()

        for account in all_accounts['accounts']:
            if account['account_holder'].lower() == account_name.lower():
                account['amount'] = balance

        self._write(all_accounts)

    def _read(self):
        data = None
        with open(self.path, 'r') as json_file:
            data = json.load(json_file)
        return data

    def _write(self, data):
        with open(self.path, 'w') as outfile:
            json.dump(data, outfile)
