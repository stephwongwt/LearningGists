#HackerRank 30 day of coding challenge. Day 7.
#!/bin/python3
#input: 1 4 3 2
#ouput: 2 3 4 1

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().rstrip().split()))
  b = [str(i) for i in a]
  print(' '.join(b[::-1]))
