#HackerRank 30 day of coding challenge. Day 8.
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
  n = int(input())
  # a = list(map(str, input().rstrip().split()))
  pb = {}
  for i in range(n):
    a = str(input()).split(" ")
    pb[a[0]] = a[1]
  while True:
    try:
      s = str(input())
      if s in pb:
        print(s+"="+pb[s])
      else:
        print("Not found")
    except (EOFError):
        break
