#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
n=int(input("Enter the number of elements : "))
l=[]
for i in range(0,n):
    k=int(input())
    if(k>100):
        l.append("over")
    else:
        l.append(k)
print(l)