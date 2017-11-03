#!/usr/bin/python 


def fibo(n):
  if not isinstance(n,int):
     print "Fibonacci only for intergers"
     return -1

  elif n==0 or n==1:
    return 1
  else:
    return (n-1)+(n-2)


print fibo(10)

print fibo(0.5)
