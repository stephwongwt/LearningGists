#HackerRank 30 day of coding challenge. Day 19.
#return the sum of all divisors of n.

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

#Complete this method
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        a = []
        for i in range(1,n+1):
            if (n%i==0):
                a.append(i)
        return sum(a)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
