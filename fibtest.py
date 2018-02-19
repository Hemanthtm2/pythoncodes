#!/usr/bin/python 


def fib(n):

  if not isinstance(n,int):
    print "Fibonocci for integers only!!!"
    return -1

  elif n==0 or n==1:

    return 1

  else:
   return (n-1)*(n-2)



#h=int(raw_input("Enter the value\n"))

print fib(3.5)
