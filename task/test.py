# count how many times each rating appears in a surey (1-5)
"""
a=list(map(int,input().split()))
count=[0]*5
for i in a:
    count[i-1]+=1
print(*count)

"""


# string print if only even or add the string to make it even 
from collections import Counter

def minop():
    n=int(input())
    s=input().strip()
    freq=Counter(s)
    op=[]
    for i in freq:
        if freq[i]%2!=0:
            op.append((i,len(s)))
            s+=i
    print(len(op))
    for i,j in op:
        print(i,j)

minop()


# Find vowels   
"""
vow={'a','e','i','o','u'}
words=input().split()
count=0
for i in words:
    if i[0].lower() in vow:
        count+=1
print(count)
""" 
# find vowels
"""
vow={'a','e','i','o','u'}
words=input().split()
count=sum(1 for i in words if i[0] in vow)
print(count)

"""

# RGB
"""
def rgb():
    s=input()
    k=int(input())
    ord=['R','G','B']
    ordid={'R':0,'G':1,'B':2}
    res=""
    for i in s:
        nidx=(ordid[i]+k)%3
        res+=ord[nidx]
    print(res)
rgb()

"""