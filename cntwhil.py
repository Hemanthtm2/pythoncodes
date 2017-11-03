#!/usr/bin/python 

def countdown(n):
  while n > 0:
    if not isinstance(n,int):
      print "Only +ve integers"
      return -1 
    

    print n
    n=n-1
print "Blastoff"


#countdown(5)
countdown(3.6)
countdown(5)
