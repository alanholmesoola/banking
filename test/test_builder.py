import unittest
from app.accountBuilder import AccountBuilder


class TestBuilder(unittest.TestCase):

    # Positive Cases
    def test_business_account(self):
        # Arrange
        observed = AccountBuilder.build(personal, Alan, 22)

        # Assert
        self.assertEqual(observed, PersonalAccount)
