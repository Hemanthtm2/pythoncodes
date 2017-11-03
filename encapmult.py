#!/usr/bin/python 

def printMult(n):

  i=1
  while i<=10:
    print i,"*",n ,"=", n*i
    i=i+1
  print 

def printMtable():

  s=1
  while s<=10:
   printMult(s);
   s=s+1

n=int(raw_input("Enter the number which you need to print multiplication table\n"))

printMult(n)
printMtable()
