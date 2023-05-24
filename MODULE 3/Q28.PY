# Write a Python program to find the repeated items of a tuple. 
list1=[]
repeated_item =0
n=int(input("enter no of element in list :"))  # FOR INPUT  NO OF ELEMENT
for i in range(n):
    element=int(input("enter element:"))   # FOR ENTER ELEMENT
    list1.append(element)
    if list1.count(element)>1: # COUNT REPETED ITEM
        repeated_item +=1
print(f"tuple is{tuple(list1)}")       # CONVERT IN TUPLE
print(f"repeated item is {repeated_item}")