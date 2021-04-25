import unittest
from app.models import Comment,Pitch,User
from app import db


class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_Daniel = User(username = 'Daniel',password = 'daniel', email = 'daniel@ms.com')
        self.new_pitch = Pitch(id=1, category = 'interview',title = 'promotion', pitch ='i love business', user = self.user_Daniel.id, upvotes = 1, downvotes = 0)
        self.new_comment = Comment(id = 1, comment= 'mmh!! Not bad', user_id=self.user_Daniel.id, pitch_id=self.new_pitch.id)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,1)
        self.assertEquals(self.new_comment.comment,'mmh!! Not bad')
        self.assertEquals(self.new_comment.user_id,self.user_Daniel.id)
        self.assertEquals(self.new_comment.pitch_id,self.new_pitch.id)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(1)
        self.assertTrue(got_comment is not None)

