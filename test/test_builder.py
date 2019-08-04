import unittest
from parameterized import parameterized

from app.studentAccount import StudentAccount
from app.businessAccount import BusinessAccount
from app.personalAccount import PersonalAccount
from app.accountBuilder import AccountBuilder


class TestBuilder(unittest.TestCase):

    @parameterized.expand([
        ("business", 'Alan', 33, BusinessAccount),
        ("personal", 'David', 32, PersonalAccount),
        ("student", 'Marie', 32, StudentAccount),
    ])
    def test_account_builder_can_build(self, acc_type, test_name, test_age, expected):
        # arrange
        account_builder = AccountBuilder()
        observed_class = account_builder.build(acc_type, test_name, test_age)

        # assert
        self.assertIsInstance(observed_class, expected)
