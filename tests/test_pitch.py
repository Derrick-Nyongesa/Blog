import unittest
from app.models import Pitch,User,Comment
from app import db

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user_Daniel = User(username = 'Daniel',password = 'daniel', email = 'daniel@ms.com')
        self.new_pitch = Pitch(id=1, category = 'interview',title = 'promotion', pitch ='i love business', user = self.user_Daniel.id, upvotes = 1, downvotes = 0)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.category,'interview')
        self.assertEquals(self.new_pitch.title,'promotion')
        self.assertEquals(self.new_pitch.pitch,'i love business')
        self.assertEquals(self.new_pitch.user_id,self.user_Daniel.id)
        self.assertEquals(self.new_pitch.upvotes,1)
        self.assertEquals(self.new_pitch.downvotes,0)

    def test_save_post(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch(self):
        self.new_pitch.save()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(get_pitch is not None)