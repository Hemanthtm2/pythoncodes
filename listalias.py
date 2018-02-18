#!/usr/bin/python 

a=[1,2,3]
b=a
print a

print b

print id(a)
print id(b)
b[0]='a'

print a

print b

