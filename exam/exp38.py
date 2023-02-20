#Create a class Publisher (name). Derive class Book from Publisher with attributes title and
# author. Derive class Python from Book with attributes price and no_of_pages. Write a
# program that displays information about a Python book. Use base class constructor invocation and
# method overriding.

class publisher:
    def __init__(self,name):
        self.name=name
class book(publisher):
    def __init__(self,name,title,auther):
        self.title=title
        self.auther=auther
        publisher.__init__(self,name)
    def display(self):

        print("Name : ",self.name)
        print("Title : ",self.title)
        print("Auther : ",self.auther)
class python(book):
    def __init__(self,name,title,auther,price,page):
        self.price=price
        self.page=page
        book.__init__(self,name,title,auther)
    def display(self):
        super().display()
        print("Price : ",self.price)
        print("Page : ",self.page)

name=input("Enter name : ")
title=input("Enter the title : ")
auther=input("Enter the auther name : ")
price=int(input("Enter the price : "))
page=int(input("Enter the page number : "))
o=python(name,title,auther,price,page)
o.display()