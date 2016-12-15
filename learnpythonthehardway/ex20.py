#!/usr/bin/env python

import ex_name
from sys import argv

# ex20: Functions and Files
ex_name.title("ex20: Functions and Files")

#Codes in the book (some words may be changed):
#
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

# Open the test file.
current_file = open(input_file)

#
print "* Output of the code in book, try to write code by yourself and run it to get the following output:"
#

print "First let's print the whole file:\n"
print_all(current_file)

# If no f.seek(0), it will not print contents of lines.
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

