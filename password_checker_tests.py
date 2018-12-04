import unittest
from password_checker import password_checker

class Tests(unittest.TestCase):
    def test_short_password(self):
        self.assertEqual(password_checker("pass"),"Password should be at least 6 characters long")

    def test_long_password(self):
        self.assertEqual(password_checker("passwordpassword"),"Password should be at most 12 characters long")

    def test_lower_case_only_password(self):
        self.assertEqual(password_checker("password"),"Password should contain at least 1 upper case letter")

    def test_upper_case_only_password(self):
        self.assertEqual(password_checker("PASSWORD"),"Password should contain at least 1 lower case letter")

    def test_lower_and_upper_case_only_password(self):
        self.assertEqual(password_checker("PASSword"),"Password should contain at least 1 number")

    def test_numbers_only_password(self):
        self.assertEqual(password_checker("123456789"),"Password should contain at least 1 lower case letter")

    def test_lower_upper_case_and_numbers_only_password(self):
        self.assertEqual(password_checker("PASSword123"),"Password should contain at least 1 character from [$#@]")
    
    def test_valid_password(self):
        self.assertEqual(password_checker("@passWORD01"), "Hooray! The password is valid")

if __name__=="__main__":
    unittest.main()  