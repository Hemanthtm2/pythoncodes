#!/usr/bin/python 

import pickle 

f1=open("pick.txt","w")

pickle.dump(10,f1)
pickle.dump([10,20,30],f1)
f1.close()

f1=open("pick.txt","r")
x=pickle.load(f1)
y=pickle.load(f1)

print x
print type(x)
print y
print type(y)

