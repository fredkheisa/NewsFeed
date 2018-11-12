import unittest
# from models import source
# Source = source.Source

class sourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):    
        '''
        Set up method that will run before every Test
        '''
        self.new_source = source(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

class sources:
    '''
    sources class to define Sources Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

if __name__ == '__main__':
    unittest.main()