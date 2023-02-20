#Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
# find sum of 2 time.
class Time:
    def __init__(self,h,m,s):
        self._h=h
        self._m=m
        self._s=s
    def __add__(self,other):
        s=self._s+other._s
        c=0
        if(s>=60):
            c=1
            s=s-60
        m=self._m+other._m+c
        c=0
        if(m>=60):
            c=1
            m=m-60
        h=self._h+other._h+c
        print(h,":",m,":",s)
print("Time 1")
s1=int(input("Enter second : "))
m1=int(input("Enter minute : "))
h1=int(input("Enter houre : "))

print("Time 2")
s2=int(input("Enter second : "))
m2=int(input("Enter minute : "))
h2=int(input("Enter houre : "))

o1=Time(h1,m1,s1)
o2=Time(h2,m2,s2)
o2.__add__(o1)