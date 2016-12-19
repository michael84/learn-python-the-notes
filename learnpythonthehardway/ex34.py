#!/usr/bin/env python
import ex_name

ex_name.title("ex34: Accessing Elements of Lists")

#Codes in the book (some words may be changed):
#
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "The aninal at 1 is %s." % animals[1]
print "The 3rd animal is %s." % animals[2]
print "The 1st animal is %s." % animals[0]
print "The animal at 3 is %s." % animals[3]
print "The 5th animal is %s." % animals[4]
print "The animal at 2 is %s." % animals[2]
print "The 6th animal is %s." % animals[5]
print "The animal at 4 is %s." % animals[4]

#####
index = ['1st', '2nd', '3rd', '4th', '5th', '6th']

for i in range(0, 6):
    print "The %s animal is at %d and is a %s." % (index[i], i, animals[i])
