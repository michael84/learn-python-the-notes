#!/usr/bin/env python
import ex_name

ex_name.title("ex32: Loops and Lists")

#Codes in the book (some words may be changed):
#

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes thru a list.
for number in the_count:
    print "This is count %d" % number

# same as above.
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we dont know what's in it.
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# The range() function only does numbers from the first to the last, not including 
# the last. So it stops at two, not three in the above. This turns out to be the most common way 
# to do this kind of loop.
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i  


#######################################################
ex_name.title("ex33: While Loops")

#Codes in the book (some words may be changed):
#
# 1. Usually a for-loop is better.
# 2. Making sure boolean test will become False at some point.
#    If not, it doesn't stop.
# 3. When in doubt, print out your test variable at the top and bottom of the while-loop
#    to see what it's doing.

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num


##########################################################
# Now let's do some Study Drills.
#
ex_name.title("ex32 - Study drills - 01")
print "Converting while-loop to a function:"
print ""

#
def number_loop(max, add):
    i = 0
    numbers = []
    
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i += add
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers:"
    for num in numbers:
        print num

# Run the function.
number_loop(4, 2)

#########
ex_name.title("ex32 - Study drills - 02")
print "Using for-loops and range() to re-write this:"
print ""

#

def number_loop_for(max, add):
    numbers = []

    for i in range(0, max + 1, add):    
        numbers.append(i)
        print "Numbers now: ", numbers
    
    print "The numbers:"
    for num in numbers:
        print num

# Run the function
number_loop_for(5, 1)
