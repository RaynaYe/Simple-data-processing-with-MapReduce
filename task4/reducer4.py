#!/usr/bin/python
import sys

prev=''
value_total=0
token=''

for line in sys.stdin:
 #   i = line.rfind(',')  # last ,
#    print "the i = "
 #   print i
    #token, value = line[:i], int(line[i + 1:])
    token, value = line.split('\t',1)
    value = int(value)
  #  print "the token = "
   # print token
    if prev==token:
        value_total += value
    else:
         if prev:
            print("{0}\t{1}".format(prev, value_total))
         value_total=value
         prev=token

print("{0}\t{1}".format(prev, value_total))