import unittest
from app.models import Comment,Pitch,User
from app import db


class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_Daniel = User(username = 'Daniel',password = 'daniel', email = 'daniel@ms.com')
        self.new_comment = Comment(comment= 'mmh!! Not bad', 'posted': datetime.datetime(2021, 4, 24, 9, 5, 7, 923394), 'user_id': None, 'pitch_id': None)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'mmh!! Not bad')
        self.assertEquals(self.new_comment.User,self.user_James)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)

