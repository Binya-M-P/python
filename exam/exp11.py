#Find biggest of 3 numbers entered.
a=int(input("enter : "))
b=int(input("enter : "))
c=int(input("enter : "))
if(a>b and a>c):
    print(a)
if(b>a and b>c):
    print(b)
else:
    print(c)