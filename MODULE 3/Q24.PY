# Write a Python program to find the length of a tuple. 
list1=[]
n=int(input("enter no of element in list :"))  # FOR INPUT  NO OF ELEMENT
for i in range(n):
    element=int(input("enter element:"))   # FOR ENTER ELEMENT
    list1.append(element)
print(f"tuple is{tuple(list1)}")       # CONVERT IN TUPLE
print(f"length of tuple is {len(list1)}") # FIND LENGTH