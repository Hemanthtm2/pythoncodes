#!/usr/bin/python 


fil=raw_input("Ente the file name\n")

try:

  f=open(fil,"r")

except IOError:
  print "There is no file named",fil
