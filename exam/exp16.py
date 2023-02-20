#Create a single string separated with space from two strings by swapping the
# character at position 1.
s1=input("Enter : ")
s2=input("Enter : ")
s=s2[0]+s1[1:]+" "+s1[0]+s2[1:]
print(s)