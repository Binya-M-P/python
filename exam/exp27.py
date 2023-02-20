#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
s=input("Enter the string : ")
if(s[-3:]=="ing"):
    s=s+"ly"
else:
    s=s+"ing"
print(s)