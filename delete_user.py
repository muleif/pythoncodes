'''
First import the os module
Create a function to take name of the user to remove to the system
call the userdel command
'''

import os
def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r " + username)
    
remove_user()