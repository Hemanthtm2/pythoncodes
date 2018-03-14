#!/usr/bin/python 
import copy

def samePoint(p1,p2):
  return(p1.x==p2.x) and (p1.y==p2.y)

class Point:
  pass


p1=Point()

p1.x=10.0
p1.y=20.0

p2=copy.copy(p1)


print samePoint(p1,p2)
