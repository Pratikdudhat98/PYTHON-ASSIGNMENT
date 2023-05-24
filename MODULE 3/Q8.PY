# Write a Python program to remove duplicates from a list. 
list1=[]
n=int(input("enter no of element in list :"))  # FOR INPUT  NO OF ELEMENT
for i in range(n):
    element=int(input("enter element:"))   # FOR ENTER ELEMENT
    if element not in list1 :              # DUPLICATE REMOVE THROUGH NOT IN USED
        list1.append (element)
print(list1)
