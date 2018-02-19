#!/usr/bin/python

#Get keys from sparse matrix ie touple of integer keys with values

mat={(0,3):1,(1,3):5,(3,2):9}

print mat.get((0,3),0)

print mat.get((0,4),0)
