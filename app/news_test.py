import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_highlight = News('Electric Vehicle Maintenance Is Super-Cheap, But The Dark Secret Is Tires','AT&T: Gift Horse, Meet Mouth','https://imageio.forbes.com/specials-images/imageserve/604fba3dc4999d6dc1fd6e1c/0x0.jpg?format=jpg&width=1200',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.news_highlight,News))


if __name__ == '__main__':
    unittest.main()
