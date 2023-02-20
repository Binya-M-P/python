#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
# to same value (c) whether any value occur in both
n1=int(input("Enter n1 : "))
l1=[]
for i in range(0,n1):
    n=int(input())
    l1.append(n)
n2=int(input("Enter n2 : "))
l2=[]
for i in range(0,n2):
    n=int(input())
    l2.append(n)
if(len(l1)==len(l2)):
    print("same length")
if(sum(l1)==sum(l2)):
    print("same sum")
for i in l1:
    if i in l2:
        print(i)