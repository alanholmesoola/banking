import unittest

from app.studentAccount import StudentAccount
from app.businessAccount import BusinessAccount
from app.personalAccount import PersonalAccount
from app.accountBuilder import AccountBuilder


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
