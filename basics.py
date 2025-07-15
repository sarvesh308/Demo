# Python Basics: Printing and Comments
"""
    print("Hello, World!") 
"""
# Python Basics: Data Types and Structures
"""
# LIST
fruits = ["apple", "banana", "orange"]
print("List:", fruits) 
fruits.append("grape") 
print("Updated List:", fruits)
fruits.remove("banana")
print("After Removal:", fruits)
fruits.sort()
print("Sorted List:", fruits)
fruits.reverse()
print("Reversed List:", fruits)
fruits.insert(1, "kiwi")
print("Inserted Kiwi:", fruits)
fruits.pop(2)
print("After Pop:", fruits)
fruits.extend(["mango", "peach"])
print("Extended List:", fruits)
fruits.clear()
print("Cleared List:", fruits)


# Tuple
coordinates = (10, 20, 30, 20)
print("Tuple:", coordinates) 
print("First Element:", coordinates[0])
print("Last Element:", coordinates[-1])
print("Slice:", coordinates[1:3])
print("Length:", len(coordinates))
print("Count of 20:", coordinates.count(20))

# Range
numbers = range(1, 6) 
print("Range:", list(numbers)) 
print("Range Start:", numbers.start)
print("Range Stop:", numbers.stop)
print("Range Step:", numbers.step)
print("Range Length:", len(numbers))


# Dictionary
student = {"name": "Sarvesh", "age": 21, "course": "CSE"}
print("Dictionary:", student)
print("Name:", student["name"])
student["age"] = 22
print("Updated Age:", student["age"])
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
student["grade"] = "A"
print("Added Grade:", student)
print("Updated Dictionary:", student)
student.pop("course")
print("After Pop Course:", student)
student.clear()
print("Cleared Dictionary:", student)

# Set
colors = {"red", "green", "blue", "red"}
print("Set:", colors) 
print("Set Length:", len(colors))
print("Is 'red' in Set", "red" in colors)
print("Is 'yellow' in Set", "yellow" in colors)
colors.add("yellow")
print("After Adding Yellow:", colors)
colors.remove("green")
print("After Removing Green:", colors)
colors.discard("blue") 
print("After Discarding Blue:", colors)
colors.clear()
print("Cleared Set:", colors)



# Frozenset
numbers = [1, 2, 3, 2]
frozen = frozenset(numbers)
print("Frozenset:", frozen)  
print("Frozenset Length:", len(frozen))
print("Is 2 in Frozenset:", 2 in frozen)
print("Is 4 in Frozenset:", 4 in frozen)

# Bytes
data = bytes([65, 66, 67, 68])
print("Bytes:", data)
print("Bytes Length:", len(data))

# Bytearray
data_array = bytearray([65, 66, 67, 68])
print("Bytearray:", data_array)
print("Bytearray Length:", len(data_array))
data_array[0] = 90
print("Modified Bytearray:", data_array)
data_array.append(69)
print("After Append:", data_array)
data_array.extend([70, 71])
print("After Extend:", data_array)
data_array.pop()
print("After Pop:", data_array)
data_array.remove(66)
print("After Remove 66:", data_array)
data_array.clear()
print("Cleared Bytearray:", data_array)

# Memoryview
data_view = memoryview(data_array)
print("Memoryview:", data_view)
print("Memoryview Length:", len(data_view))

# Boolean
is_active = True
print("Boolean Value:", is_active)
is_active = False
print("Updated Boolean Value:", is_active)
is_active = 1
print("Boolean from Integer 1:", bool(is_active))
is_active = 0
print("Boolean from Integer 0:", bool(is_active))
is_active = "True"
print("Boolean from String 'True':", bool(is_active))
is_active = ""
print("Boolean from Empty String:", bool(is_active))

# None
is_null = None
print("None Value:", is_null)

"""
# Python Basics: User Input and Output
"""
print("Printing the user details")
a= input("Enter your name: ")
b= input("Enter your age: ")
c= input("Enter your city: ")
d= input("Enter you address: ")

print("Name:", a)
print("Age:", b)
print("City:", c)
print("Address:", d)

"""

# Python Sep and End 
"""
print("Hello", "World", sep="-", end="!")

"""

# Python Operators

# Arithmetic Operators
a= 10
b=20
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Assignment Operators
c = 15
print("\nAssignment Operators:")
c += 5
print("c += 5:", c)
c -= 3
print("c -= 3:", c)
c *= 2
print("c *= 2:", c)
c /= 3
print("c /= 3:", c)
c //= 2
print("c //= 2:", c)
c %= 4
print("c %= 4:", c)
c **= 2
print("c **= 2:", c)

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("\nLogical Operators:")
print("a > 5 and b < 10:", a > 5 and b < 10)
print("a < 5 or b < 10:", a < 5 or b < 10)
print("not (a > 5):", not (a > 5))

# Identity Operators
print("\nIdentity Operators:")
print("a is b:", a is b)
print("a is not b:", a is not b)

# Membership Operators
print("\nMembership Operators:")
my_list = [1, 2, 3, 4, 5]
print("2 in my_list:", 2 in my_list)
print("6 not in my_list:", 6 not in my_list)

# Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Ternary Operator
print("\nTernary Operator:")
result = "a is greater" if a > b else "b is greater"
print("Ternary Result:", result)

# Python String slicing 
"""
a="Revature"
b=a[0:5]
print("Sliced String:", b)
c=a[::-1]
print("Reversed String:", c)
d=a[-1:-6:-1]
print("Negative Indexing Slice:", d)
f=a[1:5:2]      
print("Sliced with Step:", f)
e=a[1:7:3]
print("Sliced with Step 3:", e)

"""

# Python Scope of variables
"""
# Local Scope

def add():
    x=10
    y=20
    z=x+y
    print("Sum:", z)
print("Sum with Local variable:")
add()

# Global Scope
x = 10
y = 20
def add_global():
    global x, y #we shld use global keyword to access global variables
    z = x + y
    print("Sum with Global Variables:", z)

add_global()

# Accessing Global Variables from another file
import globalvar
print("Accessing Global Variables from globalvar.py:")
print("x:", globalvar.x)
print("b:", globalvar.b)
print("Sum", globalvar.x + globalvar.b)

"""
# Python Keywords
"""
import keyword
print("the list of keywords are:")
a=keyword.kwlist
print(len(a))
"""

# Python conditional statements
"""
#if statement
a=10
if a > 5:
    print("a is greater than 5")

# if-else statement
if a < 5:
    print("a is less than 5")
else:
    print("a is not less than 5")

# if-elif-else statement
if a < 5:
    print("a is less than 5")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is greater than 10")

# Nested if statement
if a > 5:
    print("a is greater than 5")
    if a < 15:
        print("a is also less than 15")
    else:
        print("a is greater than or equal to 15")
else:
    print("a is not greater than 5")

"""

# Python Loops
"""
# while loop
count = 0
while count<=5:
    print("Count is:", count)
    count+=1

# for loop
for i in range(1, 6):
    print("Number:", i)

# Nested for loop
for i in range(1, 3):
    for j in range(1, 4):
        print( i, j)
"""