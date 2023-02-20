#Print out all colors from color-list1 not contained in color-list2.
c1=input("Enter : ")
c1=c1.split(",")
c2=input("Enter : ")
c2=c2.split(",")
for i in c1:
    if i not in c2:
        print(i)