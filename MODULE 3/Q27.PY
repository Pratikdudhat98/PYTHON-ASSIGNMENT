# Write a Python program to replace last value of tuples in a list.
list1=[(45,63,25),(65,22,54),(74,78,95),("hello","world")]
list2=[]                             # CREATE NULL LIST
n=int(input("enter reoplace amount:")) # ENTER REPLACE AMOUNT    
for i in list1:         
    if type(i)==tuple:  # FOR DATATYPE OF LIST CHECK
        i=list(i)         # CONVERT IN LIST
        i[-1]=n            # CONVERT IN TUPLE
        i=tuple(i)       # CONVERT IN LIST
        list2.append(i)
    else:
        list2.append(i) 
print(list2)           

    
     
   