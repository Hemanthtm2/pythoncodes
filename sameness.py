#!/usr/bin/python 

class Point:

  pass


p1=Point()
p2=Point()

p1.x=3
p1.y=2
p2.x=3
p2.y=2

p2=p1

if p1 == p2:
  print True

if p1.x==p2.x:
  print True

else:

  print False

 
