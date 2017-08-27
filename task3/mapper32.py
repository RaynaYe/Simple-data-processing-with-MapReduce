#!/usr/bin/env python
import sys
for line in sys.stdin:
  print(max(map(len, line.split())))
