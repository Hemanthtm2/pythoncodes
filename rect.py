#!/usr/bin/python 


class Point:

  pass

class Rect:

  pass


box=Rect()
box.width=100.0
box.height=200.0

box.corner=Point()
box.corner.x=0.0
box.corner.y=0.0

blank=Point()
blank.x=3.0
blank.y=2.0


def printPoint(blank):
  print '('+str(blank.x)+','+str(blank.y)+')'



def findCenter(box):
  p=Point()
  p.x=box.corner.x+box.width/2.0
  p.y=box.corner.y-box.height/2.0
  return p

center=findCenter(box)
printPoint(center)




#printPoint(blank)
