#HackerRank 30 day of coding challenge. Day 13.
#locked code stub -----------
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#locked code stub -----------


#Write MyBook class
class MyBook(Book):
  def __init__(self,t,a,p):
    Book.__init__(self,t,a)
    self.price = p
  
  def display(self):
    print('Title: '+str(self.title))
    print('Author: '+str(self.author))
    print('Price: '+str(self.price))


#locked code stub -----------
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
#locked code stub -----------