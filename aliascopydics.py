#!/usr/bin/python 


oppos={"one":"two","right":"left","up":"down","top":"bottom"}

print oppos

alias=oppos

print "alias of oppos\n",alias

copy=oppos.copy()

print "copy of oppos\n",copy

copy["right"]="Test"

print "changed copy of dics\n",copy

print"original dics ie oppos\n",oppos
