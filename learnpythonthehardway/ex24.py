#!/usr/bin/env python
import ex_name

ex_name.title("ex24: More Practice")

#Codes in the book (some words may be changed):
#
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.\n'

# how about double quotes
print "how about double quotes:"
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.\n"

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "-" * 14

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# ?? jelly_beans or beans???
# Remember that inside the function the variable is temporary. 
# When you return it then it can be assigned to a variable for later. 
# A new variable named beans to hold the return value.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point = start_point / 10
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
