#!/usr/bin/python
import sys


for line in sys.stdin:
    key, value = line.split('\t', 1)
    print("{0}\t{1}".format(key, value))
