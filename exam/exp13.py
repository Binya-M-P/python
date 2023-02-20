#Create a list of colors from comma-separated color names entered by user. Display
# first and last colors.
clr=input("Enter : ")
l=clr.split(",")
print(l[0],l[-1])