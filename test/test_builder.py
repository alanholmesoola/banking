import unittest

from app.studentAccount import StudentAccount
from app.businessAccount import BusinessAccount
from app.personalAccount import PersonalAccount
from app.accountBuilder import AccountBuilder
from parameterized import parameterized


class TestBuilder(unittest.TestCase):

    # Positive Cases
    def test_person_account_is_created_using_builder(self):
        # Arrange
        account_builder = AccountBuilder()
        observed_class = account_builder.build('personal', 'Alan', 22)
        # Assert
        self.assertIsInstance(observed_class, PersonalAccount)

    def test_business_account_is_created_using_builder(self):
        # Arrange
        account_builder = AccountBuilder()
        observed_class = account_builder.build('business', 'Alan', 22)
        # Assert
        self.assertIsInstance(observed_class, BusinessAccount)

    def test_student_account_is_created_using_builder(self):
        # Arrange
        account_builder = AccountBuilder()
        observed_class = account_builder.build('student', 'Alan', 22)
        # Assert
        self.assertIsInstance(observed_class, StudentAccount)

    @parameterized([
        ("business", BusinessAccount),
        ("personal", PersonalAccount),
        ("student", StudentAccount),
    ])
    def test_accounts_using_builder_parameterised(self, userInput, expected):
        # arrange
        observed_class = account_builder.build(userInput, 'Alan', 22)
        # assert
        self.assertIsInstance(observed_class, expected)
