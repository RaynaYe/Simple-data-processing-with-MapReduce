#!/usr/bin/python
import sys
from math import log


for line in sys.stdin:
     line=line.strip().split()
     total=0
     i=2
     while i < len(line):
         total=total+int(line[i])
         i=i+1
     i=2
     output=0
     while i<len(line):
         single = float(line[i])/float(total)
         i=i+1
         output+= -(single*log(single,2))
     print ("{0}\t{1}".format(" ".join(line[0:2]),output))


















