#Find the sum of all items in a list
n=int(input("Enter the number of elements in the list : "))
l=[]
s=0
for i in range(0,n):
    k=int(input())
    l.append(k)
for i in l:
    s=s+i
#s=sum(l)
print("sum = ",s)