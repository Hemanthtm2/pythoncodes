#!/usr/bin/python 


def fact(n):

  if isinstance(n,int):
     print "Factorial is only defined for integers"
     return -1
  elif n<0:
     print "Factorial is only defined for positive integers"
     return -1

  elif n==0:
     return 1
  else:
     return n*(n-1)
     
#num=raw_input("Enter the number you want to check for factorial")

#int(num)


print fact(0.5)
#print fact(3)
#print fact(-0.5)
