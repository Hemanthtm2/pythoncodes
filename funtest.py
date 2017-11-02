#!/usr/bin/python 

#Testingfuctions
def printTwice(bruce): #parameter
  print bruce,bruce

def catTwice(one,two):

  cat=one+two

  printTwice(cat)


printTwice('Python')     #arguments->
printTwice('Python'*4)

h="Hi Iam Hemanth"

printTwice(h)


cha1="Iam"
cha2="Hemanth"

catTwice(cha1,cha2)
