import unittest
from app.models import Article,Source

class NewsTest(unittest.TestCase):
    '''
    Test class to test the instance of news articles
    '''
    def setUp(self):
        '''
        the setup method to run before every test
        '''
        self.new_article = Article('bbc','raphael','football','manchester looses','www','src','nov','scores','celebrity')
        self.new_sources = Source('BBC','Global news','general','true','cnn','ntv')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_source(self):
        self.assertTrue(isinstance(self.new_sources,Source))

if __name__=='__main__':
    unittest.main()