#!/usr/bin/python
import sys
prev=''
list=[]
key=''
def p(key,list)::
    print key, '-->',
    for (k,v) in list:
        print "(%s,%s)"%(k,v),
    print

for line in sys.stdin:
    line=line.strip().split()
    if line[0]==prev:
        if len(line) == 2:
            key = line[1]
        if len(line)==3:
            list.append((line[1],line[2]))

    else :

        if list :
            p(key,list)
        if len(line)==2:
            key=line[1]
        list=[]
        if len(line)==3:
            list.append((line[1], line[2]))
        prev=line[0]
p(key,list)