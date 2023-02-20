#Generate a list of four digit numbers in a given range with all their digits even and the
# number is a perfect square.
n1=int(input("Starting number : "))
n2=int(input("Ending number :"))
for i in range(32,100):
    if(i*i>=n1):
        break;
for j in range(i,100):
    t=j*j
    if(t>n2):
        break
    f=0
    while(t!=0):
        d=t%10
        if(d%2!=0):
            f=1
            break;
        t=t/10
        t=int(t)
    if(f==0):
        print(j*j)
