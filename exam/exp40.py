#Python program to copy odd lines of one file to other
f=open("demo.txt","r")
c=f.readlines()
k=1
l=[]
for i in c:
    if(k%2!=0):
        l.append(i)
    k=k+1
f.close()
f=open("demp2.txt","a")
for i in l:
    f.write(i)