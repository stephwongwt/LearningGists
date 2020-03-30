#HackerRank 30 day of coding challenge. Day 9.
# input: 3
# 1*2*3=6
# output: 6
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
  total = 1
  i = 1
  while i <= n:
    total *= i
    i += 1
  return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()