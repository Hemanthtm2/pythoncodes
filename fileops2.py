#!/usr/bin/python 
import os

f2=open("Mac","w")
print f2

f2.write("This is mac os file")
f2=open("Mac","r")
#f2.read("Mac")
Mac=f2.read()

print Mac
#print os.system('cat Mac')

f2.close()
