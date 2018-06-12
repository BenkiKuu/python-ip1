import unittest  # Importing the unittest module
from Password_Lock import User # Importing the contact class
import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","asdfgh890") # create contact object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.password,"asdfgh890")


# if __name__ == '__main__':
#     unittest.main()

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

# if __name__ ==  '__main__':
#     unittest.main()

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","asdfgh890",) # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

# if __name__ == '__main__':
#     unittest.main()

    # setup and class creation up here

# other test cases here
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","asdfgh890",) # new contact
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)

    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by phone password and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","asdfgh8901",) # new contact
        test_user.save_user()

        found_user = User.find_by_password("asdfgh8901")

        self.assertEqual(found_user.first_name,test_user.first_name)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","asdfgh8901",) # new contact
        test_user.save_user()

        user_exists = User.user_exist("asdfgh8901")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found contact
    #     '''
    #
    #     self.new_contact.save_contact()
    #     Contact.copy_email("0712345678")
    #
    #     self.assertEqual(self.new_contact.email,pyperclip.paste())





if __name__ == '__main__':
    unittest.main()
