#!/usr/bin/python 


prev={0:1,1:1}


def fiboTest(n):

  if prev.has_key(n):

   return prev[n]

  else:
   newval=fiboTest(n-1)+fiboTest(n-2)
   prev[n]=newval
   return newval


print fiboTest(8)
