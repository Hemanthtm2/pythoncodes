#!/usr/bin/python 


mark={"Hemanth":100,"Varada":150,"Achan":200,"Amma":250}

def sortMark(mark):

  students=mark.keys()
  students.sort()
  for student in students:

    print "%s:%d" %(student,mark[student])


print sortMark(mark)
