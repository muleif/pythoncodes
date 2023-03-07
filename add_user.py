'''
First import the os module
Create a function to take name of the user to add to the system
call the useradd command
'''

import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo useradd " + username)

new_user()