#!/usr/bin/python 

class Point:

  pass

blank=Point()
blank.x=3.0
blank.y=2.0
print blank.x
print blank.y


print '('+str(blank.x)+','+str(blank.y)+')'

print blank.x*blank.y
print blank
print id(blank)

def printPoint(p):
   print '('+str(p.x)+','+str(p.y)+')'






printPoint(blank)
