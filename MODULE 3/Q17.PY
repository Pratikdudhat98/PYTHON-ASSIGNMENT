# Write a Python program to check whether a list contains a sub list 
list1=[]
sublist=[]
n=int(input("no of element in list:"))  # FOR ENETR NO OF ELEMENT
for i in range(n):
    element=input("enter element:")  # FOR ENTER ELEMENT
    list1.append(element)
print(list1)
a=int(input("no of element in sublist:"))
for i in range(a):
    elements=input("enter element:")  # FOR ENTER ELEMENT IN SUBLIST
    sublist.append(elements)
print(sublist) 
if set(sublist).intersection(set(list1)):   #convert in set for condition
    print("sublist contain in list")  
else:
    print("sublist not contain in list")     