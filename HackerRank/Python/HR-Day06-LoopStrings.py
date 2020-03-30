#HackerRank 30 day of coding challenge. Day 6.
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  n = int(input())
  for i in range(0,n):
    a = list(str(input()))
    b,c="",""
    for j in range (0, len(a)):
      if (j % 2 == 0):
        b = b + a[j]
      else:
        c = c + a[j]
    print(b+" "+c)
