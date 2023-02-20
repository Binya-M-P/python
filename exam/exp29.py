#Construct following pattern using nested loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n=int(input("Enter the length of longest line : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

i=n-1
while(i>=1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
    i=i-1