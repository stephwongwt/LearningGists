#HackerRank 30 day of coding challenge. Day 14.
#Find the largest absolute difference between any numbers in the list
class Difference:
  def __init__(self, a):
    self.__elements = a
    
  # Add your code here
  def computeDifference(self):
    e = self.__elements
    mD = 0
    cD = 0
    for i in range(len(e)):
      for n in e:
        if n != e[i]:
          cD = abs(e[i]-n)
          if cD > mD:
            mD = cD
    self.maximumDifference = mD
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
