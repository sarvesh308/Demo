"""
# Input/Output & Variables

print("Hello, World!")

# 2 no as input and sum

x,y=2,5
print(x+y)

# area of circle
import math
r=5
area=math.pi * r**2
print("Area of circle:", area)

# Swap to numbers
a,b=5,10
print("Before swapping: a =", a, ", b =", b)
a,b=b,a
print("After swapping: a =", a, ", b =", b)

# Conditional Statements

# Even or Odd
num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

# check leap year
year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap Year")
else:
    print("Not a leap year")

# Largest of 3 numbers

a,b,c=10,20,30
if a>b>c:
    print("A is greatest")
elif b>a>c:
    print("B is greatest")
else:
    print("C is greatest")


# Loop

n=10
for i in range(1,n+1):
    print(i)

i=1
while n>10:
    print(i)
    i+=1

"""
