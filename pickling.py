#!/usr/bin/python 

import pickle 

f=open("test.pck","w")

pickle.dump(12.4,f)
pickle.dump([10,20,30],f)
f.close()
f=open("test.pck","r")
x=pickle.load(f)

print type(x)
f.close()

