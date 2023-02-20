#Find gcd of 2 numbers.
n1=int(input("Enter : "))
n2=int(input("Enter : "))
i=1
gcd=1
while(i<=n1 or i<=n2):
    if(n1%i==0 and n2%i==0):
        gcd=i;
    i=i+1
print(gcd)