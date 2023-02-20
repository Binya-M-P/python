#Create a string from given string where first and last characters exchanged. [eg: python -
# > nythop]
s1=input("Enter the str : ")
t=s1[0]
t2=s1[-1]
s=s1[-1]+s1[1:-1]+s1[0]
print(s)