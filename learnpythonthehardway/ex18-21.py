#!/usr/bin/env python
import ex_name

# ex18: Names, Variables, Code, Functions
ex_name.sub_title("ex18: Names, Variables, Code, Functions")

# Functions do: name pieces of code, take arguments and make mini-scripts (or tiny commands).

#Codes in the book (some words changed):
#
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."

print "* Output of the code in book, try to write your code and run it to get the following output:"
print_two("Hello", "World")
print_two_again("Hello", "Again")
print_one("One")
print_none()

#

# ex19: Functions and Variables
ex_name.sub_title("ex19: Functions and Variables")

#Codes in the book (some words changed):
#
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheesees!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
#
print "* Output of the code in book, try to write your code and run it to get the following output:"
#
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#

# ex20: Functions and Files
ex_name.sub_title("ex20: Functions and Files")

#Codes in the book (some words changed):
#


