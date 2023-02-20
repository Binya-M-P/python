#Accept a list of words and return length of longest word.
n=int(input("Enter the number of words : "))
l=[]
for i in range(0,n+1):
    k=input()
    l.append(k)
long=0
for i in l:
    if(len(i)>long):
        long=len(i)
print(long)