#!/usr/bin/python 


def strcomp(word):

  if word < "banana":
    print "Your word,"+ word + ",comes before banana"
  elif word > "banana":
    print "Your word,"+ word + ",comes after banana"
  else:
    print "Yes we have no banana's"


w=raw_input("Enter the word\n")

strcomp(w)
