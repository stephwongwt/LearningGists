#https://www.hackerrank.com/challenges/taum-and-bday/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    total = 0
    c = b+w
    if bc > (wc+z):
        total = (c*wc)+(b*z)
    elif wc > (bc+z):
        total = (c*bc)+(w*z)
    else:
        total = (b*bc)+(w*wc)
    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
