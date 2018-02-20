#!/usr/bin/python 
import os

f3=open("kernel.dat","w")


f3=open("kernel.dat","r")

print os.system('dmesg | less >> kernel.dat')

print os.system('cat kernel.dat')



#kernel.dat=f3.read()


f3.close()
