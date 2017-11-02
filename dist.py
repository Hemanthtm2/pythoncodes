#!/usr/bin/python 

import math

def distance(x1,x2,y1,y2):

  dx=x2-x1
  dy=y2-y1
  dsqaured=dx**2+dy**2
  result=math.sqrt(dsqaured)
  return result 

def area2(xc,yc,xp,yp):

  radius=distance(xc,yc,xp,yp)
  area=math.pi*radius**2
  return area

print distance(5,4,6,7)

print area2(2,3,4,5)
