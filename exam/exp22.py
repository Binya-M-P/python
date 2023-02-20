#Generate Fibonacci series of N terms
n=int(input("Enter the value of n : "))
n1=-1
n2=1
for i in range(0,n):
    n=n1+n2
    n1=n2
    n2=n
    print(n)