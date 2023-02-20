#Write a Python program to read specific columns of a given CSV file and print the content
# of the columns.
import csv

f=open("dep.csv","r")
ff=csv.DictReader(f)
for i in ff:
    print(i["Series_reference"])