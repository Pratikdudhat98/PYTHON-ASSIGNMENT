# Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
dic1={1:897,6:897,14:457,25:879,12:564,89:7458}
list1=[]                # CREATE EMPTY LIST
dic1=dic1.items()             
dic1=list(dic1)             # CONVERT LIST OF TUPLE INTO LIST
for i in dic1:
    if i[0]>1 and i[0]<15: 
        list1.append(i)          # ADD ELEMENT IN LIST AND AFTER CONVERT IN DICTIONARY
list1=dict(list1)     
print(list1)
        