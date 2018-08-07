#HackerRank 30 day of coding challenge. Day 16.
#Convert input to int, and print it. If error, print "Bad String"
#!/bin/python3

import sys

S = input().strip()
try:
    print(str(int(S)))
except ValueError:
    print("Bad String")
