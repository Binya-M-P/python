#Store a list of first names. Count the occurrences of ‘a’ within the list
n=int(input("enter the number : "))
l=[]
for i in range(0,n):
    k=input()
    l.append(k)
print(l)
c=0
for i in l:
    for j in i:
        if(j=="a"):
            c=c+1
print(c)

