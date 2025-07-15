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
