# Write a Python program to count the occurrences of each word in a given sentence .
n=input("ENTER SENTENCE:")
n=n.split(" ")             # CONVERT INTO LIST WITH SPLIT BECAUSE OF WORD OCCURANCE
dict1={}
for i in n:                  # FOR CHECK ALL ELEMENT IN LIST
    if i in dict1:            # FOR CHECK IN DICTIONARY ELEMENT OCCUER OR NOT
        dict1[i]+=1
    else:
        dict1[i]=1
for key in dict1.keys():
    print(f"{key} :{dict1[key]} ")        # PRINT IN DICTIONARY 




