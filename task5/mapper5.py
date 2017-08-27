#!/usr/bin/python
import sys
for line in sys.stdin:
    line=line.split()
    #str_list = ' '.join(map(str, a))
    a = ' '.join(line[0:3])
    print ('{0}\t{1}'.format(int(line[3]), a))
