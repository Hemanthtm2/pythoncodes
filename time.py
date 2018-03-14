#!/usr/bin/pyrhon 
class Time:
  pass


time=Time()
time.hours=11
time.minutes=59
time.seconds=30

def printTimes(time):
  print time.hours,':',time.minutes,':',time.seconds

def addTime(t1,t2):

  sum=Time()
  sum.hours=t1.hours+t2.hours
  sum.minutes=t1.minutes+t2.minutes
  sum.seconds=t1.seconds+t2.seconds
  return sum
  

printTimes(time)

currentTime=Time()
currentTime.hours=9
currentTime.minutes=14
currentTime.seconds=30

breadTime=Time()

breadTime.hours=3
breadTime.minutes=35
breadTime.seconds=0


doneTime=addTime(currentTime,breadTime)

printTimes(doneTime)
