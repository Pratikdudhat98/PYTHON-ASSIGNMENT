# Write a Python program to create a tuple with numbers.
list1=[]
n=int(input("no of element in list:"))  # FOR ENETR NO OF ELEMENT
for i in range(n):
    element=int(input("enter element:"))  # FOR ENTER ELEMENT
    list1.append(element)
print(f"tuple is {tuple(list1)}")   # CONVER IN TUPLE AND PRINT

