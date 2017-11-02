#!/usr/bin/python 

def comp(x,y):

  if x>y:
     return 1
  elif x==y:
     return 0
  else:
     return -1

n1=raw_input("Enter the value for x\n")
n2=raw_input("Enter the valur for y\n")

print comp(n1,n2)
