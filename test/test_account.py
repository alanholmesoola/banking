import unittest
from app.account import Account


class TestAccount(unittest.TestCase):

    # Positive Cases
    def test_user_can_deposit(self):
        # Arrange
        account = Account("Alan", "33")
        expected_result = 100

        # Act
        account.deposit(100)
        observed = account.balance

        # Assert
        self.assertEqual(observed, expected_result)

    def test_user_can_withdraw_amount_in_account(self):
        # Arrange
        account = Account("Alan", "33")
        account.balance = 200
        expected_result = 100

        # Act
        account.withdraw(100)
        observed = account.balance

        # Assert
        self.assertEqual(observed, expected_result)

    def test_user_can_withdraw_amount_not_in_account(self):
        # Arrange
        account = Account("Alan", "33")
        account.balance = 100
        expected_result = "Sorry insufficent funds"

        # Act
        observed = account.withdraw(101)

        # Assert
        self.assertEqual(observed, expected_result)
