'''
Import the subprocess module
Import the os module
Create a function to take name of the user to add to the groups
Use the subprocess to get the list of groups available to add the user
call the usermod command
'''

import subprocess
import os

def add_user_togroup():
    username = input("Enter the name of the user that you want to addto a group: ")
    output = str(subprocess.Popen("groups", stdout=subprocess.PIPE).communicate()[0])
    print("Enter a list of groups to add the user to ")
    print("The list should be seperated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    chosengroups = str(input("Groups: "))

    output = output.split(" ")
    chosengroups = chosengroups.split(" ")
    print("Add To:")
    found = True
    groupstring = ""


    for grp in chosengroups:
        for existinggrp in output:
            if grp == existinggrp:
                found = True
                print("- Existing Group : " + grp)
                groupstring = groupstring + grp + ","
        if found is False:
            print("- New Group : " + grp)
            groupstring = groupstring + grp + ","
        else:
            found = False
    
    groupstring = groupstring[:-1] + " "
    confirm = ""
    while confirm != "Y" and confirm != "N" :
        print("Add user '" + username + "' to these groups?(Y/N)")
        confirm = input().upper()
    if confirm == "N":
        print("User '" + username + "' not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG "+ groupstring + username)
        print("User '" + username + "' added")

add_user_togroup()