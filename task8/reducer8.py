#!/usr/bin/python
import sys
avg_max=0
avg_max_name=''
for line in sys.stdin:
    line=line.strip()
    name,avg=line.split('\t',1)
    if avg > avg_max:
        avg_max=avg
        avg_max_name=name
print avg_max_name,avg_max


