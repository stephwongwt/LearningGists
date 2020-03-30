#HackerRank 30 day of coding challenge. Day 11.
#input 6x6 2D array, print the largest sum of integers in an hourglass shape.
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  arr = []

  for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

  fin = -100
  for i in range(len(arr)-2):
    for j in range(len(arr[i])-2):
      tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
      if tmp > fin:
        fin = tmp
  print(fin)