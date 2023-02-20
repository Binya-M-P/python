#Count the number of characters (character frequency) in a string.
s=input("Enter the string : ")
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
for i,j in d.items():
    print(i,j)