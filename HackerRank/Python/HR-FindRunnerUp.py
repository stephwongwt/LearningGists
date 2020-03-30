# HackerRank Challenge. Find the Runner-Up Score!
# Given N and a list A[i], find the runner up.
# 2 <= n <= 10
# -100 <= i <= 100

# input
## 5
## 2 3 6 6 5
# output
## 5

# input
## 4
## 57 57 -57 57
# output
## -57

if __name__ == '__main__':
  n = int(input())
  arr = map(int, input().split())
  winner, runnerup = -100, -100
  for i in arr:
    if (i > winner):
      runnerup = winner
      winner = i
    elif (winner > i > runnerup):
      runnerup = i
  print(runnerup)
