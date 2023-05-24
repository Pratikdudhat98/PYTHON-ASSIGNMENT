# Write a Python program to convert a list to a tuple.
list1=[]
n=int(input("enter no of element in list :"))  # FOR INPUT  NO OF ELEMENT
for i in range(n):
    element=int(input("enter element:"))   # FOR ENTER ELEMENT
    list1.append(element)
print(f"list is {list1}")   # CONVERT INTO LIST    
print(f"tuple is{tuple(list1)}")       # CONVERT IN TUPLE