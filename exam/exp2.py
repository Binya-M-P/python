s=int(input("Enter the starting year : "))
e=int(input("Enter the ending year : "))
for i in range(s,e+1):
    if((i%400==0)or((i%4==0)and(i%100!=0))):
        print(i)