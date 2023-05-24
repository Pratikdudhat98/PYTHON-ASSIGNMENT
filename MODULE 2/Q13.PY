# Write a Python program to count the number of characters (character Frequency) in a string.
n=input("ENTER SENTENCE:")
dict1={}
for i in n:                  # FOR CHECK ALL ELEMENT IN LIST
    if i in dict1:            # FOR CHECK IN DICTIONARY ELEMENT OCCUER OR NOT
        dict1[i]+=1
    else:
        dict1[i]=1
for key in dict1.keys():
    print(f"{key} :{dict1[key]} ")        # PRINT IN DICTIONARY