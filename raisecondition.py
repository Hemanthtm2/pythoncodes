#!/usr/bin/python 

def inputNum():
  num=input("Enter a number")

  if num==13:

    raise ValueError,'13 is a bad number'
  return num

inputNum()



