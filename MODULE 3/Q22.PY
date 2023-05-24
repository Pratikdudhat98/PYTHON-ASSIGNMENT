# Write a Python program to convert a tuple to a string.
demo=[]
n=int(input("no of element in list:"))  # FOR ENETR NO OF ELEMENT
for i in range(n):
    element=input("enter element:")  # FOR ENTER ELEMENT
    demo.append(element)
print(f"tuple is {tuple(demo)}")   # CONVER IN TUPLE AND PRINT
print(" ".join(demo)) # CONVERT INTO STRING