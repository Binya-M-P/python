#Get a string from an input string where all occurrences of first character replaced with
# ‘$’, except first character.
# [eg: onion -> oni$n]
s=input("enter the string : ")
t=s[0]
s=s.replace(t,"$")
print(t+s[1:])