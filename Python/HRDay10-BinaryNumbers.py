#HackerRank 30 day of coding challenge. Day 10.
#input number, change to binary, count number of consecutive 1s.
# input: 13
# 13 = 1101
# output: 2
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    a = list(bin(n)[2:])
    c = []
    d = 0
    if '0' in a:
      for i in range(len(a)):
        if (a[i] == '1'):
          d += 1
        else:
          c.append(d)
          d = 0
      c.append(d)
      print(max(c))
    else:
      print(len(a))