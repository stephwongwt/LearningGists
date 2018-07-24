#HackerRank 30 day of coding challenge. Day 6.
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  n = int(input())
  a = [str(input()), str(input())]
  for i in range(0, len(a)):
    a[i] = list(a[i])
    b,c="",""
    for j in range (0, len(a[i])):
      if (j % 2 == 0):
        b = b + a[i][j]
      else:
        c = c + a[i][j]
    print(b+" "+c)
    
