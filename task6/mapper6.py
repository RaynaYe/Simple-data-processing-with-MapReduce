#!/usr/bin/python
import sys
prev02=''
list=[]
value=0
for line in sys.stdin:
    line=line.split()
    if line[0:2]==prev02:
        list.append((line[3]))

    else:
        if prev02:
            print ('{0}\t{1}'.format(' '.join(prev02),' '.join(list)))
        prev02=line[0:2]
        list=[]
        list.append(line[3])
print ('{0}\t{1}'.format(' '.join(prev02), ' '.join(list)))

