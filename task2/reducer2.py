#!/usr/bin/python
import sys

prev = ""
counter = 0

for line in sys.stdin:
    i = line.rfind(',')  # last ,
    line, v = line[:i], int(line[i + 1:])
    if line == prev:
        counter += v
    else:
        if 1 == counter and prev:
            print prev
        counter = v
        prev = line

if counter==1 and prev:
    print prev

