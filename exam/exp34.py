#Create Rectangle class with attributes length and breadth and methods to find area and
# perimeter. Compare two Rectangle objects by their area.

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        return a
    def perimeter(self):
        p=2*(self.length+self.breadth)
        return p

l1=int(input("Enter the length : "))
b1=int(input("Enter the breadth : "))
o1=Rectangle(l1,b1)
l2=int(input("Enter the length : "))
b2=int(input("Enter the breadth : "))
o2=Rectangle(l2,b2)
a=o1.area()
b=o2.area()
if(a>b):
    print("Area 1")
elif(b>a):
    print("Area 2")
else:
    print("same")