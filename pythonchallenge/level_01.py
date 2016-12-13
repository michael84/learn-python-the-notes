#!/usr/bin/python

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print s
print len(s)
print ""

alpha = []
for i in range(ord('a'), ord('z')+1):
    alpha.append(chr(i))
print alpha

result = []
for letter in s:
#    result = []
    if letter in alpha:
        letter_index = alpha.index(letter) + 2
        #print letter_index
        if letter_index <= 25:
            #print alpha[letter_index]
            result.append(alpha[letter_index])
        elif letter_index == 26:
            result.append('a')
        elif letter_index == 27:
            result.append('b')
    else:
        result.append(letter)
print ''.join(result)

# using string.maketrans() is the best way.
from string import maketrans

abc = 'abcdefghijklmnopqrstuvwxyz'
cde = 'cdefghijklmnopqrstuvwxyzab'

trans_table = maketrans(abc, cde)
leve01_url = "map"
print
print "new level 2 url is:"
print leve01_url.translate(trans_table) 
