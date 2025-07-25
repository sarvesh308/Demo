# Lambda function example

# Lambda function to double a number
s=lambda x: x*2
print("Output:",s(5))

# Multiple arg

a=lambda x,y:x+y
print(a(3,2))

# using map()

num=[1,2,3,4,5]
b=list(map(lambda x:x**2,num))
print(b)

# Filter
a1=list(filter(lambda x:x%2==0,num))
print(a1)

# sorted()

st=['ravi','suresh','kumar','sai']
sor=sorted(st,key=lambda x: len(x))
print(sor)

# Str to upper case

up=list(map(lambda x:x.upper(),st))
print(up)

a2=list(filter(lambda x:x.startswith('s'),st))
print(a2)