# -*- coding: utf-8 -*-
"""
Exercise 7: Some Counting - 20 Marks
"""
#the following is the list of variables
a=0
b=0
c=0
d=0
e=0

print("\nzero to fifty:")
for a in range(0,51):#counts from 0 to 50
    print(a)
    
print("\nfifty to zero:")
for b in reversed(range(0,51)):#counts from 50 to 0
    print(b)
    
print("\nthirty to fifty:")
for c in range(30,51):#counts from 30 to 50
    print(c)
    
print("\nfifty to ten:")
for d in reversed(range(10,51,2)):#counts from 50 to 10 in decrements of 2
    print(d)
    
print("\none hundred to two hundred:")
for e in range(100,201,5):#counts from 100 to 200 in increments of 5
    print(e)
