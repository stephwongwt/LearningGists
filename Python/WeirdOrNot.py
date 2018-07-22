#HackerRank. if n is odd, it's weird. if it is even and (6 >= N >= 20), it's weird.
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    if (N % 2 == 1): #odd
        print("Weird")
    else:
        if (6 <= N <= 20):
            print("Weird")
        else:
            print("Not Weird")
