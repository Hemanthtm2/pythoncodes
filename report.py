#!/usr/bin/python 

wages={"Hemanth":12.5,"Varada":32.4,"Amma":2.4,"Achan":43.8}

def genReport(wages):

  students=wages.keys()
  students.sort()
  for student in students:
    print "%-20s : %12.2f" % ( student, wages[student] )



genReport(wages)
