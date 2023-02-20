#Create a package graphics with modules rectangle, circle and sub-package 3D-graphics with
# modules cuboid and sphere. Include methods to find area and perimeter of respective figures
# in each module. Write programs that finds area and perimeter of figures by different importing
# statements. (Include selective import of modules and import * statements)

#import graphics;
from graphics import threedg,circle,rectangle;
import graphics.threedg.cuboid as c
import graphics.threedg.sphere as t

print("Rectangle :")
l=int(input("Enter the length : "))
w=int(input("Enter the width : "))
rectangle.area(l,w)
rectangle.perimeter(l,w)

print("Circle :")
l=int(input("Enter the radius : "))
circle.area(l)
circle.perimeter(l)

print("cuboid :")
l=int(input("l : "))
b=int(input("b : "))
h=int(input("h : "))
c.area(l,b,h)
c.perimeter(l,b,h)

print("Cuboid :")
r=int(input("Enter the radius : "))
t.area(r)
t.perimeter(r)
