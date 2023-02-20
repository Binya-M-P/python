#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to
# compare the area of 2 rectangles.

class Rectangle:
    def __init__(self,length,width):
        self._length=length
        self._width=width
        self.area=self._length*self._width
    def __lt__(self,other):
        if(self.area<other.area):
            print("Area 2")
        elif(self.area>other.area):
            print("area 1")
        else:
            print("Same")

print("Rectangle 1")
l1=int(input("Enter the length"))
w1=int(input("Enter the width"))
print("Rectangle 2")
l2=int(input("Enter the length"))
w2=int(input("Enter the width"))
o1=Rectangle(l1,w1)
o2=Rectangle(l2,w2)

o1.__lt__(o2)