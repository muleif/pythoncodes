'''
First import the os module
Create a function to take user input of whether to install or remove a package
For install call the sudo apt install command
For remove call the sudo apt remove command
If on Red Hat Enterprise, use yum instead of apt
'''

import os

def install_or_remove_packages():
    iOrR = "" 
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
        
    if iOrR == "I": 
        iOrR = "install"
        
    elif iOrR == "R": 
        iOrR = "remove"
        
    print("Enter a list of packages to install") 
    print("The list should be separated by spaces, for example:") 
    print(" package1 package2 package3") 
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program") 
    packages = input().lower() 
    
    if packages == "default": 
        packages = ""
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get upgrade -y")
        
    if iOrR == "install":
        os.system("sudo apt-get install " + packages + " -y")
        
    elif iOrR == "remove": 
        while True: 
            print("Purge files after removing? (Y/N)") 
            choice = input().upper() 
            
            if choice == "Y":
                os.system("sudo apt-get " + iOrR + " " + packages + " -y") 
                os.system("sudo apt-get autoremove -y") 
                break
            
            elif choice == "N":
                os.system("sudo apt-get " + iOrR + " " + packages + " -y") 
                break

#Cleans the environment after an uninstall    
def clean_environment(): 
        os.system("sudo apt autoremove") 
        os.system("sudo apt autoclean")

#Updates the default modules
def update_environment():
    os.system("sudo apt update") 
    os.system("sudo apt upgrade") 
    os.system("sudo apt update --security")

install_or_remove_packages()