#!/usr/bin/python
import sys
for line in sys.stdin:
    line = line.strip()
    tokens=line.split()
    a=''

    for i in range(len(tokens)-2):
        a=tokens[i:i+3]
        str_list=' '.join(map(str,a))
        print ('{0}\t{1}'.format(str_list,1))
