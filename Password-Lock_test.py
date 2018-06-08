 import unittest  # Importing the unittest module
 from contact import Contact # Importing the contact class
 import pyperclip

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com") # create contact object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Contact.contact_list = []
