# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
str1=input("ENTER STRING :") # FOR INPUT
if len(str1)>=3 and str1.endswith("ing") : # ends with 'ing' then add 'ly' 
    print(str1.replace("ing","ly"))
elif len(str1)>=3 and not(str1.endswith("ing")) :    # add 'ing' at the end of a given string 
    print(str1+"ing")
else:
    print("leave it unchanged")
