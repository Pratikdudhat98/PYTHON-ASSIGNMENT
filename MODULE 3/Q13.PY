# Write a Python program to convert a list of characters into a string.
list1=[]
n=int(input("no of element in list:"))  # FOR ENETR NO OF ELEMENT
for i in range(n):
    element=input("enter element:")  # FOR ENTER ELEMENT
    list1.append(element)
print(list1)
print(" ".join(list1))    # CONVERT INTO STRING