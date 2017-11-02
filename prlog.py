#!/usr/bin/python 
import math
def printLog(x):

  if x<0:
    print "Err..Positive numbers only!!!"
    return 

  result=math.log(x)
  print "result=",result


printLog(20)
printLog(-3)
