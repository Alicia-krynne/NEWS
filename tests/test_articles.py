import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the  articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(1234,'news from all  over  the  word ','/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

