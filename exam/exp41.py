#Write a Python program to read each row from a given csv file and print a list of string
import csv
f=open("dep.csv","r")
ff=csv.reader(f)
l=[]
for i in ff:
    l.append(i)
print(l)