#!/usr/bin/python 

prev={0:1,1:1}

def fibon(n):

  if prev.has_key(n):
     return prev[n]

  else:
    newval=fibon(n-1)+fibon(n-2)
    prev[n]=newval
   # print prev.keys()
   # print prev.items()
    return newval




print fibon(50)




