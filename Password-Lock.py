import pyperclip #

class Contact:
    """
    class that generates new instances of contacts
    """
    contact_list = []
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)
    def __init__(self,first_name,last_name,number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
