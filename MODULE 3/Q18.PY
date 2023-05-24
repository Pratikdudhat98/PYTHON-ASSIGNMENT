# Write a Python program to split a list into different variables. 
list1=[]
for i in range(5):
    element=int(input("enter element:"))   # FOR ENTER ELEMENT
    if element not in list1 :              # DUPLICATE REMOVE THROUGH NOT IN USED
        list1.append (element)
print(list1)
A,B,C,D,E= list1  # SPLIT IN VARIABLE
print(A)          # PRINT ALL VARIABLE
print(B)
print(C)
print(D)
print(E)