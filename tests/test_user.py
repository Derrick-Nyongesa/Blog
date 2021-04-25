import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username= 'Daniel', email= 'daniel@ms.com', pass_secure= 'pbkdf2:sha256:150000$EecCkf44$4ef006d4910f8644d053a473f6e0e302c0e9251de743d9646675f8ac528c1455', bio= None, profile_pic_path= None)

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.pass_secure

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('campmulla'))