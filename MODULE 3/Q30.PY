# Write a Python program to unzip a list of tuples into individual lists. 
list1=[(25,45),(45,89),(78,74),(62,54),(51,23)]
list1=dict(list1)     #FIRST CONVERT IN DICTIONERY
a=list1.keys()        # FIND KEY 
b=list1.values()     # FIND VALUE
a=list(a)          # CONVERT IN LIST
b=list(b)
print(a)        # PRINT 
print(b)