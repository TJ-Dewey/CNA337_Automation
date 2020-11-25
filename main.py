# This is the template code for the CNA337 Final Project
# TJ Dewey tjdewey@student.rtc.edu
# CNA 337 Fall 2020
# Base code template furnished by Zachary Rubin, zrubin@rtc.edu
# Stackoverflow.com and docs.python.org for pinging using os module

import os
from Server import Server

def print_program_info():
    print("Server Automator v0.13 by T.J. Dewey")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    myEC2 = Server("3.15.229.69") #EC2 address
    status = myEC2.ping()
    print(status)    
