# This is the template code for the CNA337 Final Project
# TJ Dewey tjdewey@student.rtc.edu
# CNA 337 Fall 2020
# Base code template furnished by Zachary Rubin, zrubin@rtc.edu
# Stackoverflow.com and docs.python.org for pinging using os module
# Stackoverflow.com for Running Powershell functions in python with subprocess (not used)
# docs.microsoft.com for powershell excecution policy (not used)
# Paramiko examples at programcreek.com
# help with Paramiko @ youtube: "Automating SSH using python | by using Paramiko module" by Exploit Blizzard
# Paramiko documents: "Using Paramiko to control an EC2 instance" @ Mainly Data
# With tutoring from Zak Rubin

from Server import Server

def print_program_info():
    print("Server Automator v0.17 by T.J. Dewey")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    myEC2 = Server("3.15.229.69") #EC2 address
    status = myEC2.ping()
    print(status)    
    myEC2.connect()
