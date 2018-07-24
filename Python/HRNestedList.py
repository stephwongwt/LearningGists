#HackerRank python challenge. https://www.hackerrank.com/challenges/nested-list/problem
#Return the second lowest score, sort alphabetically if there are multiple results.

import operator

if __name__ == '__main__':
  stuarr = []
  lowestscore = 100.0
  seclowestscore = 100.0
  for _ in range(int(input())):
    name = input()
    score = float(input())
    stuarr.append([name,score])
    if (score < lowestscore) and (score != lowestscore):
      seclowestscore = lowestscore
      lowestscore = score
    elif (lowestscore < score < seclowestscore) and  (score != seclowestscore):
      seclowestscore = score
  newArr = sorted(stuarr, key=operator.itemgetter(0))
  [print(i[0]) for i in newArr if i[1] == seclowestscore]
