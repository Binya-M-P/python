#Count the occurrences of each word in a line of text.
line=input("Enter the line")
l=line.split(" ")
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
for i,j in d.items():
    print(i,":",j);