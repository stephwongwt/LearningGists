#HackerRank 30 day of coding challenge. Day 20.
#given a list of numbers, use bubble sort algorithm to sort in ascending order, count the number of swaps made.
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0
for i in range(0, n):
  for j in range(0, n-1):
    if (a[j] > a[j + 1]):
      a[j], a[j + 1] = a[j + 1], a[j]
      swaps+=1
  if (swaps == 0):
    break
print("Array is sorted in "+str(swaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]))
