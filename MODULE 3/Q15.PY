# Write a Python program to find the second smallest number in a list. 
list1=[]
n=int(input("enter no of element in list :"))  # FOR INPUT  NO OF ELEMENT
for i in range(n):
    element=int(input("enter element:"))   # FOR ENTER ELEMENT
    list1.append(element)
print(list1)
list1.sort()  # FOR ASCENDING ORDER
print(f"secound smallest no is {list1[1]}")     # PRINT SECOUND SMALLEST NO