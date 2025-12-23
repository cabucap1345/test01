from getpass import getpass
import requests
import json
import sys
from tabulate import tabulate
##import shutil
import time
#import datetime
#import os
#import aiobastion
#import asyncio
#import http.client
from prettytable import PrettyTable
#import textwrap
#import logging
#logging.basicConfig(level=logging.DEBUG)
from requests.exceptions import HTTPError
import csv
#import http.client
#http.client.HTTPConnection.debuglevel = 1
import subprocess
#from pythonping import ping
#from scapy.all import sr1, IP, ICMP
#from ping3 import ping
#import platform
#import wmi
from subprocess import call
#import urllib.parse
from importlib.resources import path
from multiprocessing.sharedctypes import Value
from optparse import Values
import time
from turtle import delay
from urllib import request
import requests
import readchar
import pathlib
from datetime import datetime
from csv import writer
import pprint
from colorama import init
from termcolor import colored
import os
import shutil
import pandas as pd
#fljdkshfkjldhslkfds
1######-------------------------------------------------------------------
PAM_BASE_URL = "https://pam.brian.com.vn"

def authenticate():
    try:
        PAM_AUTH_ENDPOINT = PAM_BASE_URL + "/passwordvault/api/auth/radius/logon"
        usernamePAM = input("Username: ")
        password = getpass()
        internal_otp = input("Input your OTP: ")
        passwordPAM = password + internal_otp
        data = {
            "username": usernamePAM,
            "password": passwordPAM,
            "concurrentSession": "true"
        }
        response = requests.post(PAM_AUTH_ENDPOINT, data=data, timeout=10)
        response.raise_for_status()
        return response.text.strip('"')        
    except requests.exceptions.RequestException as e:
        print("Error! Please check and try login again.")
        print(e)
        sys.exit(1)
    

######-------------------------------------------------------------------
if __name__ == "__main__":
    while True:
        print("Please select an option:\n")
        print("0. Authenticate\n")

        print("1.1. Get Safe")
        print("1.2. Create safe")
        print("1.3. Add safe member template")
        print("1.4. Add safe member manual\n")

        print("2.1. Get Accounts & export to host.csv")
        print("2.2. Link ")
        print("2.3. Unlink")
        print("2.4. Reconcile")
        print("2.5. Verify")
        print("2.6. Change Immediately")
        print("2.7. Delete")
        print("2.8. Link DB")
        print("2.9. Resume\n")

        print("3.1. Bulk Account\n")
        
        print("4.1. Create/Delete My Request\n")

        print("q. Quit")
 
        start_time = time.time()
        user_input = input("Enter your choice: ")
 
        if not user_input:
            if time.time() - start_time >= 300:  # 5 minutes
                print("No input received, automatically selecting option 2.")
                user_input = "2"
                 
        if user_input == "0":
            token = authenticate()
            print("\n### AUTHENTICATED success ###\n")
            #print(token)
            
        elif user_input == "1.1":
            get_safe()

        elif user_input == "1.2":
            create_safe_member()

        elif user_input == "1.3":
            add_safe_member()

        elif user_input == "1.4":
            add_safe_member_manual()

        elif user_input == "2.1":
            get_account()    

        elif user_input == "2.2":
            link_account()    

        elif user_input == "2.3":
            unlink_account() 

        elif user_input == "2.4":
            reconcile()    

        elif user_input == "2.5":
            verify_account()    

        elif user_input == "2.6":
            change_imme()    

        elif user_input == "2.7":
            delete_account()    
        elif user_input == "2.8":
            link_account_db()    

        elif user_input == "2.9":
            resume_account() 

        elif user_input == "3.1":
            bulk_account()

        elif user_input == "4.1":
            create_delete_myrequest()

#        elif user_input == "3":
#            requestid = input("Input your RequestID want to approve: ")
#            if 'TOKEN' in locals():
#                approve_requests(TOKEN, requestid)
#            else:
#                print("Please authenticate first.")
#        elif user_input == "4":
#            requestid = input("Input your RequestID want to reject: ")
#            if 'TOKEN' in locals():
#                reject_requests(TOKEN, requestid)
#            else:
#                print("Please authenticate first.")
        if user_input.lower() == 'q':
            print("Exiting program...")
            break
#        else:
#            print("Invalid choice. Please try again.")        
            
     

    
