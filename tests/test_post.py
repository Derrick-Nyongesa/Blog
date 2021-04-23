import unittest
from app.models import Post,User
from app import db

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user_Daniel = User(username = 'Daniel',password = 'daniel', email = 'daniel@ms.com')
        self.new_post = Post(id=1, category = 'interview',title = 'deloitte', pitch ='i love business', user = self.user_Daniel)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id,'1')
        self.assertEquals(self.new_post.category,'interview')
        self.assertEquals(self.new_post.title,'delloitte')
        self.assertEquals(self.new_post.pitch,'i love business')
        self.assertEquals(self.new_post.User,self.user_Daniel)

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)