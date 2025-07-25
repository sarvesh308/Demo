# input types

# Norml input
a=input()
print(a)

# intger input
b=int(input())
print(b)

# float input
c=float(input())  
print(c)

# multiple inputs in a single line
d=input().split()
print(d)

e=map(int, input().split())
print(list(e))

# list input
f=list(map(int, input().split()))
print(f)

# input with seprator handling
g=input().split(',')
print(g)

# input with seprator handling and conversion
h=list(map(int, input().split(',')))    
print(h)

# vlidating input with try-except
try:
    i = int(input("Enter an integer: "))
    print(f"You entered: {i}")
except ValueError:  
    print("That's not a valid integer!")

# input as matrix or 2D list
j = [list(map(int, input().split())) for _ in range(3)]
print(j)

# input as matrix or 2D list with custom separator
k = [list(map(int, input().split(','))) for _ in range(3)]  
print(k)

# striping or cleaning input
l = input().strip()  # removes leading and trailing whitespace
print(l)

# converting input to a set
m = set(map(int, input().split()))
print(m)

# converting input to a tuple
n = tuple(map(int, input().split()))        
print(n)

# converting input to a lowercase string
o = input().lower()
print(o)
# converting input to an uppercase string
p = input().upper() 
print(p)
# converting input to a title case string
q = input().title() 
print(q)
"C:\Users\sarve\inputtypes.py"