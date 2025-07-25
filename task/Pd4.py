# Practices Day4

# Exception
"""
class UserNotFound(Exception):
    def __init__(self,msg="User not found in the list"):
        super().__init__(msg)

list=['a','b','c','d']

def findUser(name):
    if name not in list:
        raise UserNotFound(f"User not found in list")
    return f"User {name} is found"
try:
    name_inp=input("Enter the name to find:")
    res=findUser(name_inp)
    print(res)
except UserNotFound as e:
    print(f"Error {e}")

"""
#  Delete a file
"""
import os

fp='fil.txt'
if os.path.exists(fp):
    os.remove(fp)
    print(f"File removes successfully")
else:
    print(f"File doesnt exists")

"""

# Email validation
"""
import re

def mailcheck(mail):
    pat=r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    res=re.match(pat,mail)
    return res is not None
mail="sarveshtraveller@gmail.com"
print("valid" if mailcheck(mail) else "Invalid")

"""

#  URL validation
"""
import re

def urlcheck(url):
    pat=r'^[\w{4,5}]+://[\w.-]+\.\w+.$'
    res=re.match(pat,url)
    return res is not None
url=("https://www.google.com")
print("valid" if urlcheck(url) else "Invalid")

"""

# Write to csv file
"""
import csv

data=[
    ['name','age','loc'],
    ['sarvesh',21,'chennai'],
    ['varun',13,'chennai']
]

with open('data.csv','w') as f:
    writer=csv.writer(f)
    writer.writerows(data)
print("csv file written successfully")

"""
# Capitalize first letter

from collections import *

dig=['sarvesh','varun','vani','ravi']
a=[i.capitalize() for i in dig]
print(list(a))
    



