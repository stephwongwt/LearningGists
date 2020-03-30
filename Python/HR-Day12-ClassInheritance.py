#HackerRank 30 day of coding challenge. Day 12.
#locked code stub -----------
class Person:
  def __init__(self, firstName, lastName, idNumber):
    self.firstName = firstName
    self.lastName = lastName
    self.idNumber = idNumber
  def printPerson(self):
    print("Name:", self.lastName + ",", self.firstName)
    print("ID:", self.idNumber)
#locked code stub -----------


class Student(Person):
  #   Class Constructor
  #   
  #   Parameters:
  #   firstName - A string denoting the Person's first name.
  #   lastName - A string denoting the Person's last name.
  #   id - An integer denoting the Person's ID number.
  #   scores - An array of integers denoting the Person's test scores.
  #
  # Write your constructor here
  def __init__(self,a,b,c,d):
    Person.__init__(self,a,b,c)
    self.scores = d    

  #   Function Name: calculate
  #   Return: A character denoting the grade.
  #
  # Write your function here
  def calculate(self):
    avg = sum(self.scores)/len(self.scores)
    if (90 <= avg <= 100):
      return 'O'
    elif (80 <= avg < 90):
      return 'E'
    elif (70 <= avg < 80):
      return 'A'
    elif (55 <= avg < 70):
      return 'P'
    elif (40 <= avg < 55):
      return 'D'
    else:
      return 'T'


#locked code stub -----------
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
#locked code stub -----------