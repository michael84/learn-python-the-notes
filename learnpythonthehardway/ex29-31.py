#!/usr/bin/env python
import ex_name

ex_name.title("ex29: What If")

#Codes in the book (some words may be changed):
#

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

#########################################################

ex_name.title("ex30: Else And If")

#Codes in the book (some words may be changed):
#
people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we should take buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

# Study Drills:
print ""
print "Study Drills:"

if people < cars and people < buses and cars < buses:
    print "Less people here."
elif people > cars > buses:
    print "Too many people here."
elif people < cars and people > buses:
    print "Take bus!"
else:
    print "Hard to make dicision."

# Python only take the fist True.
if people > cars:
    print "This is False."
elif people < cars:
    print "First True."
elif people > buses:
    print "2nd True."
elif cars > buses:
    print "3rd True."

##################################################
ex_name.title("ex31: Making Decisions.")

#Codes in the book (some words may be changed):
#

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door = raw_input("> ")

if door == "1":
    print "There is a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"


