from app.account import Account

import unittest

class TestAccount(Account.TestCase):

#Positive Cases

    def deposit(self):
        # Arrange
        account = Account("Alan","33")
        expected_result = "100"
        
        # Act
        account.deposit(100)
        observed = account.balance
        
        # Assert
        self.assertEqual(observed, expected_result)