import pyperclip

class User:
    """
    class that generates new instances of Users
    """
    user_list = []
    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)
    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def delete_user(self):

        '''
        delete_contact method
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a contact that matches that password.

        Args:
            password: password to search for
            Returns :
            Credentials of person that matches the password.
            '''

        for user in cls.user_list:
            if user.password == password:
                return user

    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.password == password:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list

    # @classmethod
    # def copy_email(cls,number):
    #     contact_found = Contact.find_by_number(number)
    #     pyperclip.copy(contact_found.email)
