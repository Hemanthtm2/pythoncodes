#!/usr/bin/python 
import os

f1=open("linux.dat","w")

print f1

f1.write("This file is generated by OS")
f1=open("linux.dat","r")

print os.system('cat linux.dat')

f1.close()