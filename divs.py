#!/usr/bin/python 

def isDivisible(x):

  if int(x)%2==0:
    return True
  else:
    return False

num=raw_input("Enter the value to check eveness\n")

print isDivisible(num)
