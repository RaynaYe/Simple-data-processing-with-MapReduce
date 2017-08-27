#!/usr/bin/python
import sys
for line in sys.stdin:
    line=line.strip().split()
    mark_list=[]
    sum = 0
    avg=0
    if len(line)>5:
        for i in range(2,len(line)):
            mark=line[i][1:(len(line[i])-1)]
            mark=mark.split(',')
            mark_list.append(mark[1])
        for i in range(len(mark_list)):
            sum = sum + int(mark_list[i])
            avg=float(sum)/float(len(mark_list))
        print ('{0}\t{1}'.format(line[0],avg))
