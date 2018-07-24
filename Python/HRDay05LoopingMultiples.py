#HackerRank 30 days of coding. Day 5.
#Given n, print first 10 multiples.
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
      print(str(n)+" x "+str(i)+" = "+str(n*i))
