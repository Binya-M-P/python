#From a list of integers, create a list removing even numbers.
n=int(input("Enter the number of integers : "))
l=[]
for i in range(0,n):
    k=int(input())
    l.append(k)
p=[]
for i in l:
    if(i%2!=0):
        p.append(i)
print(p)