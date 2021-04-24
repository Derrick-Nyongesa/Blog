import unittest
from app.models import Pitch,User
from app import db

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user_Daniel = User(username = 'Daniel',password = 'daniel', email = 'daniel@ms.com')
        self.new_pitch = Pitch(id=1, category = 'interview',title = 'deloitte', pitch ='i love business', user = self.user_Daniel)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,'1')
        self.assertEquals(self.new_pitch.category,'interview')
        self.assertEquals(self.new_pitch.title,'delloitte')
        self.assertEquals(self.new_pitch.pitch,'i love business')
        self.assertEquals(self.new_pitch.user,self.user_Daniel)

    def test_save_post(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)