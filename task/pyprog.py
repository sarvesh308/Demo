# Program 1 Hello World
"""
print("Hello, World!")
"""

# Program 2 Calculator
"""
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
"""
# Program 3 Temperature Conversion
"""
c=float(input("Enter temperature in Celsius: "))
a=(c * 9/5) + 32
print("Temperature in Fahrenheit:", a)
f=float(input("Enter temperature in Fahrenheit: "))
b=(f - 32) * 5/9
print("Temperature in Celsius:", b)
"""
# Program 4 Age calculator
"""
print("Welcome to the Age Calculator!")
yob=int(input("Enter your year of birth: "))
from datetime import datetime
current_year = datetime.now().year
age = current_year - yob
print("Your age is:", age)
"""

# Python simple intrest calculator
"""
print("Welcome to the Simple Interest Calculator!")
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time in years: "))
si = (p * r * t) / 100
print("Simple Interest:", si)
"""

# Python Area calculator
"""
print("Welcome to the Area Calculator!")
import math
radius=float(input("Enter radius of the circle: "))
area=math.pi*radius**2
print("Area of the circle:",area)

length=float(input("Enter length of the rectangle: "))
width=float(input("Enter width of the rectangle: "))
rect=length*width
print("Area of the rectangle:", rect)

height=float(input("Enter height of the triangle: "))
base=float(input("Enter base of the triangle: "))
tri=(height*base)/2
print("Area of the triangle:", tri)

"""
# Python Grade calculator
"""
print("Welcome to the Grade Calculator!")
grade = float(input("Enter your grade: "))
if grade>=90:
    print("Your grade is A")
elif grade>=80:
    print("Your grade is B")
elif grade>=70:
    print("Your grade is C")
elif grade>=60:
    print("Your grade is D")
elif grade>=50:
    print("Your grade is E")
else:
    print("Your grade is F")
"""

# Python tip calculator
"""
print("Welcome to the Tip Calculator!")
bill= float(input("Enter the total bill amount: "))
tippercentage = float(input("Enter the tip percentage: "))
tipamount = (tippercentage/100)*bill
print("Tip amount:", tipamount)
print("Total amount to be paid:", bill + tipamount)
"""

# python even or odd checker
"""
print("Welcome to the Even or Odd Checker!")
num = int (input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
"""

# Python Leeap Year Checker
"""
print("Welcome to the Leap Year Checker!")"
year = int(input("Enter a year: "))
if(year%4==0 and year%100 !=0) or (year%400==0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
"""

# Python number guessing game
"""
print("Welcome to the Number Guessing Game!")"
import random 

num =int(input("Enter a number between 1 and 100: "))
randint =int(random.randint(1,100))
while num != randint:
    if num < randint:
        print("Too low! Try again.")
    elif num > randint:
        print("Too high! Try again.")
    num = int(input("Enter a number between 1 and 100: "))
print("Congratulations! You've guessed the number:", randint)

"""

# Python muletiplication table
"""
print("Welcome to the Multiplication Table Generator!")"
n=int(input("Enter a number to generate its multiplication table: "))
for i in range(1,13):
    print(f"{n} x {i} = {n*i}")
"""

# Python prime number checker
"""
print("Welcome to the Prime Number Checker!")"
num= int(input("Enter a number to check if it is prime: "))
is_prime = True
if num <= 1:
    is_prime = False
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
"""

# Python factorial calculator
"""
print("Welcome to the Factorial Calculator!")
num= int(input("Enter a number to calculate its factorial: "))
fact=1
for i in range(1,num+1):
    fact*=i
print(f"The factorial of {num} is {fact}")

"""

# Python Sum of Digits
"""
print("Welcome to the Sum of Digits Calculator!")
n = int(input("Enter number: "))
sod=0
for i in range(1, n + 1):
    sod += i
print(f"The sum of digits from 1 to {n} is {sod}")

"""

# Python pattern printing
"""
print("Welcome to the Pattern Printing Program!")
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" *" * i)
"""

# String Operations

# Palindrome Checker
"""
print("Welcome to the Palindrome Checker!")
str = input("Enter a string to check if it is a palindrome: ")
if str == str[::-1]:
    print(f"{str} is a palindrome.")
else:
    print(f"{str} is not a palindrome.")

"""

# String Reversal
"""
print("Welcome to the String Reversal Program!")
str= input("Enter a string to reverse: ")
revstr= str[::-1]
print("Reversed String:", revstr)

"""

# String Character Count
"""
print("Welcome to the Character Count Program!")
n=str(input("Enter a string: "))
char=input("Enter character to count: ")
count=n.count(char)
print(f"The character '{char}' appears {count} times in the string '{n}'.")

"""

# String Word Count
""" 
print("Welcome to the Word Count Program!")
sent = input("Enter a sentence: ")
count=len(sent.split())
print("count:", count)

"""
# Password strength checker
"""
print("Welcome to the Password Strength Checker!")"
pas= input("Enter password:")
if len(pas)>=6 and any(c.isupper() for c in pas) and any(c.isdigit() for c in pas):
    print("password is strong")
else:
    print("password is weak")

"""

# case convertor
"""
print("Welcome to the Case Converter!")
str= input("Enter a string: ")
print("Uppercase:",str.upper())
print("Lowercase:",str.lower())
print("Titlecase:",str.title())

"""

# Anagram Checker
"""
print("Welcome to the Anagram Checker!")
s1=input("Enter first string: ")
s2=input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

"""


# List Operations
""" 
print("Welcome to the List Operations Program!")
list=[1,2,3]
list.append(5)
print("append:",list)
list.insert(3,4)
print("insert:",list)
list.remove(2)
print("remove:", list)
list.pop()
print("pop:", list)
list.sort()
print("sort:", list)
list.reverse()
print("reverse:", list)

"""

# Duplicate Removal from List
"""
print("Welcome to the Duplicate Removal Program!")
list1 = [1, 2, 3, 4, 4, 5, 5]
a=list(frozenset(list1))
print("List with duplicates removed:", a)

"""

# List statistics
"""
print("Welcome to the List Statistics Program!")
list = [1, 2, 3, 4, 5]
print(max(list))  # Maximum value
print(min(list))  # Minimum value
print(sum(list))  # Sum of all elements
print(len(list))  # Length of the list
print(sum(list) / len(list))  # Average of the list

"""

# List merging
"""
print("Welcome to the List Merging Program!")
a= [1, 2, 3]
b= [4, 5, 6]
c=sorted(a+b)
print("Merged and Sorted List:", c)

"""

# Matrix operations
"""
print("Welcome to the Matrix Operations Program!")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result = A[i][j] + B[i][j]
print("Matrix Addition: ",result)

"""
# Matrix multiplication 
"""
print("Welcome to the Matrix Operations Program!")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result = A[i][j] * B[i][j]
print("Matrix Addition: ",result)
"""

# Function Operations
"""
print("Welcome to the Function Operations Program!")
# Functoin without parameters

def f1():
    print("Hello, World!")
f1()

# Function with parameters
def f2(name):
    print("Hello,",name)
f2("Sarvesh")

# Function with return value

def f3(a,b):
    return a+b
res=f3(3,5)
print("Sum:", res)

# Function with default parameters
def f4(name="Demo"):
    print("Hello,",name)
f4()
f4("Sarvesh")

# Function with multiple return values
def f5():
    name="Sarvesh"
    age=20
    return name,age
n,a=f5()
print("Name:", n,"| Age:", a)

# Function with variable number of arguments
def f6(*num):
    return sum(num)
res=f6(1,2,3,4,5)
print("Sum of variable arguments:", res)

# Function with keyword arguments
def f7(**details):
    for key,value in details.items():
        print(key,":",value)
f7(name="Sarvesh", age=21, city="Chennai")

"""

# Function practices
"""

def get_marks():
    mark = []
    for i in range(5):
        m = int(input(f"Enter marks for subject {i+1}: "))
        mark.append(m)
    return mark

def sum_mark(mark):
    total = sum(mark)
    return total

a = get_marks()
b = sum_mark(a)

print("Marks:", a)
print("Total Marks:", b)

"""

# Arrays
"""
import array

num = array.array("i",[1,2,3,4,5])
print(num)
print(num[2])
print(num[-1])
del num[1:3]
print(num)
del num
arr=array.array('i',[])
print(arr)
arr.append(10)
arr.append(20)
arr.insert(1,30)
print(arr)
print(arr.tolist())

"""

# Lamda Function
"""
# Lambda Add

ad=lambda x,y:(x+y)
print(ad(3,5))

# Lambda Exponents

n=lambda x:x**2
print(n(5))

# Lambda Printing numbers

li=[lambda arg = x : arg*10 for x in range(1,5)]
for i in li:
    print(i())

# Lambda Even checker

check= lambda x:"Even" if x%2==0 else "Odd"
print(check(5))
print(check(4))

# Lambda with multiple statements

calc=lambda x,y:(x+y,x*y)
res=calc(3,5)
print(res)

# Lambda Filter 
n=[1,2,3,4,5,6,8]
eve=filter(lambda x: x%2==0,n)
print(list(eve))

# Lambda map

a=[1,2,3,4,5,6]
b=map(lambda x:x*2,a)
print(list(b))

# Lambda Reduce
from functools import reduce
a=[1,2,3,4,5,6]
c=reduce(lambda x,y:x*y,a)
print(c)

"""

# Decorators
"""
# Manual Decorator

def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

def greet():
    print("Hello!")


decorated_greet = my_decorator(greet)
decorated_greet()
print("Sarvesh")


# Decorator using @Decorator

def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
print("Sarvesh")

"""

# OOP Concepts
"""
# Class & Object

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Sarvesh",21)
print(p1.name)
print(p1.age)


# Class n Obj With default parameters
class dog:
    species='canine'
    def __init__(self,name="Hello",age=21):
        self.name=name
        self.age=age

dg1=dog()
dg2=dog("hello",5)

print(dg1.name)
print(dg2.age)


# using _str_() function inside the class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} is {self.age} years old."

p1 = Person("John", 36)

print(p1)

"""
"""
class animal:
  def __init__(self, name):
    self.name = name

  def species(self):
    return "Hello"

class Dog(animal):
  def sound(self):
    return "Woof!"
  
a=animal("Generic method")
d=Dog("buddy")

print(a.name)
print(d.name)
print(d.sound())

print(a.species())

print(d.sound())
print(d.species())

"""

# Super keyword
"""
class parent():
    def show(self):
        print("Inside parent")

class child(parent):
    def show (self):
        super().show()
        print("Inside child")

obj=child()
obj.show()

"""

# Encapsulation
"""
# Public 

class public:
    def __init__(self):
        self.name= "sarvesh"
    def dispname(self):
        print(self.name)

obj = public()
obj.dispname()

# Protected

class protected:
    def __init__(self):
        self.__age=21
    def dispage(self):
        print(self.__age)

obj1=protected()
obj1.dispage()

# Private

class private():
    def __init__(self):
        self.___salary=35000
    def dispsal(self):
        print(self.___salary)

obj2=private()
obj2.dispsal()

"""

# Polymorphism
"""
print(len("Hello"))
print(len([1,2,3]))

print(max(1,2,3))
print(max('s','a','d'))

def add(a,b):
    return a+b
print(add(3,2))
print(add("hello,","World"))
print(add([1,2],[2,3]))

# Polymorphism practices

class shape:
    def area(self):
        return "undefined"
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    
shapes = [Rectangle(12,13),Circle(12)]
for shape in shapes:
    print(f"area:{shape.area()}")
        
# Polymorphism types

# Duck Typing 
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

def animal_sound(animal):
    animal.speak()

c = Cat()
d = Dog()

animal_sound(c)  # Meow
animal_sound(d)  # Woof


# Operator overloading

print(2 + 3)           # Addition for integers
print("Hi" + "Sarvesh")  # Concatenation for strings
print([1, 2] + [3, 4])   # List merging


# Method Overriding
class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def start(self):
        print("Car engine started!")

v = Vehicle()
c = Car()

v.start()  # Starting vehicle...
c.start()  # Car engine started!


# Method Overloading ( does'nt support in python we can achieve it by *args and *kwargs)

class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5))       # 5
print(m.add(5, 3))    # 8
print(m.add(5, 3, 2)) # 10

"""
# Python module
"""
import math

print(math.sqrt(24))
print(math.pi)
print(max(1,2))
print(min(3,5))
print(abs(-3.2))
print(pow(2,3))
print(math.ceil(2))
print(math.floor(123/2))

"""

# JSON 
"""
# Python obj to JSON string
import json
data={
    "name":"sarvesh",
    "age":21,
    "city":"chennai"
}
js=json.dumps(data)
print(js)

# JSON string to python obj

js='{"name": "sarvesh", "age": 21, "city": "chennai"}'
data=json.loads(js)
print(data["name"])

# JSON Read a file

with open("data.json","r") as file:
    content=json.load(file)
    print(content)

# JSON file write

data={
    "name":"sarvesh",
    "age":21,
    "city":"chennai",
    "married": False
}
with open("Output.json","w") as file:
    cont=json.dump(data,file,indent=4)

"""

# Logging

"""
# Loggin in python 

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("this is a debug message")
logging.info("this is info message")
logging.warning("Warning message")
logging.error("error message")
logging.critical("Critical message")

"""

# Collection module

"""
# Normal count
text = "banana"
count_dict = {}

for char in text:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print(count_dict)  # {'b': 1, 'a': 3, 'n': 2}

# Counter

from collections import *

fruit = ["Apple", "Banana", "Grapes", "Apple"]
count = Counter(fruit)
print(count)


# Normal Dict

d = {}
key = 'apple'

if key in d:
    d[key] += 1
else:
    d[key] = 1

print(d)

# Default Dict

d=defaultdict(int)
d['a']+=1
print(d['a'])
print(d['b'])

# Noraml ordering
d = {'banana': 3, 'apple': 1, 'cherry': 2}
print(d)

# OrderedDict

od = OrderedDict()
od['banana'] = 3
od['apple'] = 1
od['cherry'] = 2
print(od)

# Normal Tuple
person = ("Sarvesh", 21)
print(person[0])  # Not readable

# Namedtuple
Person = namedtuple('Person', ['name', 'age'])
p = Person("Sarvesh", 21)
print(p.name, p.age)

# Normal Deque

queue = []
queue.insert(0, 'first')  # insert at beginning
queue.append('last')      # insert at end
print(queue)

# Deque()

dq = deque()
dq.append('last')        # O(1) orderly arrange
dq.appendleft('first')   # O(1) add to the left
print(dq)

# Normal merging
a = {'x': 1}
b = {'x': 2}
merged = a.copy()
merged.update(b)
print(merged)

# Chain map

a = {'x': 1,'y':2}
b = {'x': 2,'z':3}
cm = ChainMap(a, b)
print(cm['x'],cm['y'],cm['z'])

"""

# Regex

"""
import re

word = "Hello, World"
pattern = r"Hello"  # raw string pattern is preferred
wo = re.match(pattern, word)
print(wo)


def exph(text):
    patterns = [
        r'\b\d{3}-\d{3}-\d{4}\b',              # Format: 123-456-7890
        r'\b\(\d{3}\)\s*\d{3}[-\s]\d{4}\b',     # Format: (123) 456-7890 or (123)456 7890
        r'\b\d{3}\.\d{3}\.\d{4}\b',             # Format: 123.456.7890
    ]

    ph = []
    for pat in patterns:
        ph.extend(re.findall(pat, text))  # Corrected: Loop over `patterns`
    return ph

# Test string
text = "You can call me at 805-627-1145 or (888)324 4456 or 123.456.7890"
print(exph(text))

"""







# Exception Handling
"""
try:
    result=10/0
except ZeroDivisionError:
    print("Cant divide zero")

# try..except

try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Done handling exception")
"""
# Multiple exception
"""
try:
    num=int(input("Enter a number"))
    print(10/num)
except(ValueError,ZeroDivisionError,TypeError) as e:
    print(f"An Error occured: {e}")
else:
    print("Code is exceuted")

finally:
    print("Exception is solved")

# Custom Exception 

class CustomError(Exception):
    pass
class ValidationError(Exception):
    def __init__(self,message,code=None):
        super().__init__(message)
        self.code=code
def validateAge(age):
    if age<0:
        raise ValidationError("Age Cannot be Negative",code="NEGATIVE_AGE")
    if age>150:
        raise ValidationError("Age Seems Unrealistic",code="UNREALISTIC_AGE")

try:
    validateAge(-5)
except ValidationError as e:
    print(f"Validation failed: {e}")
    print(f"Error code: {e.code}")

"""

# File Handling
"""
# Reading files

with open ('fil.txt','r') as f:
    cont=f.read()
    print(cont)

with open ('fil.txt','r') as f:
    for line in f:
        a=line.strip()
        print(a)

with open('fil.txt','r') as f:
    c=f.readlines()
    print(c)

# Writing operations

with open('output.txt','w') as f:
    f.write("Hello iam writing")

lines=["l1\n","l2\n","l3\n"]
with open('output.txt','w') as f:
    f.writelines(lines)

with open('output.txt','a') as f:
    f.write("\n Appended text")

"""

# Os
"""
# Check if file exists

import os
if os.path.exists('fil.txt'):
    print("File exists")

# Get size of file

size=os.path.getsize('fil.txt')
print(size)

# Get file modification time

import time
mt=os.path.getmtime('fil.txt')
rt=time.ctime(mt)
print(rt)

"""

# JSON files
"""
# Reading json file
import json
with open('data.json','r') as f:
    c=json.load(f)
    print(c)

# Writing json file

data={"name":"demo","age":30}
with open('out.json','w') as f:
    json.dump(data,f,indent=2)
"""

# Binary Files
"""
# Reading binary file

with open('img.jpg','rb') as f:
    a=f.read()
    print(a)

# Writing a Binary file

"""

""""
with open('out.jpg','wb') as f:
    f.write(a)

"""