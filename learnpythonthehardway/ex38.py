#!/usr/bin/env python
import ex_name

ex_name.title("ex38: Doing Things to Lists")

#Codes in the book (some words may be changed):
#

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# If < 10 is better idea?
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There is %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # print the 2nd item
print stuff[-1] # print the last item
print stuff.pop() # pop up the last item
# join(' ', stuff), using ' ' join items in stuff.
# But must be ' '.join(stuff) in code.
print ' '.join(stuff) # what? cool!! split <=> join
# Similar to range(3, 5), it will not touch 5.
print '#'.join(stuff[3:5]) # the 3rd and 4th items.
