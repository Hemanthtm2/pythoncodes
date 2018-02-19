#!/usr/bin/python 

import random

def rlist(n):
  s=[0]*n

  for i in range(n):
     s[i]=random.random()
  return  s



print rlist(8)
