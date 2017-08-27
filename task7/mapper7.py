#!/usr/bin/python
import sys
for line in sys.stdin:
    line=line.strip().split()
    if len(line)==3:
        print ("{0}\t{1}".format(line[1],line[2]))
    else:
        print ("{0}\t{1}".format(line[1],' '.join(map(str,line[2:]))))
