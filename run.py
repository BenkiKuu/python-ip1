#!/usr/bin/env python3.6
from Password_Lock import User

def create_user(fname,lname,pword):
    '''
    Function to create a new User
    '''
    new_user = User(fname,lname,pword)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_by_password(password)

def display_users(user):
    '''
    method that returns the user list
    '''
    return cls.user_list

def check_existing_users(password):
    '''
    Function that check if a user exists with that password and return a Boolean
    '''
    return User.user_exist(password)

# def check_existing_users(password):
#     '''
#     Function that check if a user exists with that password and return a Boolean
#     '''
#     return User.user_exist(password)


def main():
    print("Hello Welcome to your Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : nw - New User, du - display users, log -log in, ex -exit the Password Locker")

            short_code = input().lower()

            if short_code == 'nw':
                print("New User")
                print("-"*10)

                print ("First name ....")
                f_name = input()

                print("Last name ...")
                l_name = input()

                print("Password ...")
                pword = input()



                save_users(create_user(f_name,l_name,pword,)) # create and save new user.
                print ('\n')
                print(f"New User {f_name} {l_name} created")
                print ('\n')

            elif short_code == 'du':

                if display_users():
                        print("Here is a list of all users")
                        print('\n')

                        for user in display_users():
                            print(f"{user.first_name} {user.last_name}")

                            print('\n')
                else:
                        print('\n')
                        print("There are no users saved yet")
                        print('\n')

            elif short_code == 'log':

                    print("Please enter your Password")

                    search_password = input()
                    if check_existing_users(search_password):
                            search_user = find_user(search_password)
                            print(f"{search_user.first_name} {search_user.last_name}")
                            print('You are Loged in')
                            print('-' * 20)

                            # print(f"Phone number.......{search_contact.number}")
                            # print(f"Email address.......{search_contact.email}")
                    else:
                            print("You have no account")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("Please use the short codes")

if __name__ == '__main__':

    main()
