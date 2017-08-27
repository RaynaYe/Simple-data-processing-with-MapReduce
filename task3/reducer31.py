#!/usr/bin/python
import sys
lmax ,max_line = 0, ''
wmax=0


for line in sys.stdin:
    length,line = line.split(',',1)
    length = int(length)


    if length > lmax:# max value
        lmax,max_line = length,line

    for token in line.split():
        if wmax<len(token):
            wmax=len(token)

print(lmax)
print(wmax)