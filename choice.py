#!/usr/bin/python 


def dispatch(choice):

  if choice=='A':
    funcA()
  elif choice=='B':
    funcB()
  else:
    print "invalid choice"

def funcA():
  print "Valid choice A"
def funcB():
  print "Valide choice B"

ch=raw_input("Enter your choice....!\n")

dispatch(ch)
