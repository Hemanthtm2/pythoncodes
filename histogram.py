#!/usr/bin/python 

lettercount={}

for letter in "Mississippi":

  lettercount[letter]=lettercount.get(letter,0) + 1



print lettercount
