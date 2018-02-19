#!/usr/bin/python 

dics={"one":"Hemanth","two":"Varada","Three":"Amma","four":"Achan"}

print "Key-value of dictiionary"
print dics

print "Value of the key one"

print dics["one"]

print "Delete key two"

del dics["two"]
print "print dictionary for verification"
print dics


dics["two"]="Varada"

print "keys of dictionary"

print dics.keys()

print "Values of dictionary"

print dics.values()

print "items in the dictionary"

print dics.items()


print "Has key methord"


print dics.has_key("four")
