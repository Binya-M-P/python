#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
# read the CSV file and display the content.
import csv
h=["id","name"]
d=[
    {"id":1,"name":"a"},
    {"id":2,"name":"b"},
    {"id":3,"name":"c"}
]
try:
    f=open("dep2.csv","w")
    w=csv.DictWriter(f,fieldnames=h)
    w.writeheader()
    for i in d:
        w.writerow(i)

except IOError:
    print("Error")
