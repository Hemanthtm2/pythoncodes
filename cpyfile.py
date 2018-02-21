#!/usr/bin/python 

def copyFile(of,nf):

  f1=open(of,"r")
  f2=open(nf,"w")

  while True:
    text=f1.read(50)
    if text == "":
      break
    f2.write(text)

  f1.close()
  f2.close()
  return


print copyFile("test.txt","testnew.txt")
  

