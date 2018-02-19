#!/usr/bin/python 
import random

def inrange(n):
 s=[0]*n

 for i in range(n):
   s[i]=random.random()

 print s

inrange(8)
