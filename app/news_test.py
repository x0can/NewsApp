import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """
    def setUp(self):
        """

        Set up method thst will run before every Test
        """
        self.new_news = News(1234,"abcdefghijkl","abcdefjakknkd","bahadhJHDHD","HDSAJFJHBFBADFB","afaf","afafa")

    def tearDown(self):
        """
        tearDown method for cleaning up after each test has run
        """
        pass

    def test_init(self):
        self.assertEqual(self.new_news.id,"id")
        self.assertEqual(self.new_news.name,"name")
        self.assertEqual(self.new_news.author,"author")
        self.assertEqual(self.new_news.title,"title")
        self.assertEqual(self.new_news.description,"description")
        self.assertEqual(self.new_news.publishedAt,"publishedAt")
        self.assertEqual(self.new_news.content,"content")


if __name__ == "__main__":
    unittest.main()            