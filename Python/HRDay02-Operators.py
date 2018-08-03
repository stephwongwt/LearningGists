#HackerRank. 30 days of coding challenge. Day 2
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    print("The total meal cost is "+str(round(meal_cost+(meal_cost*(tip_percent/100))+(meal_cost*(tax_percent/100))))+" dollars.")

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
