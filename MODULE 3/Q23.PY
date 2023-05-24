# Write a Python program to check whether an element exists within a tuple.
demo=[]
n=int(input("no of element in list:"))  # FOR ENETR NO OF ELEMENT
for i in range(n):
    element=input("enter element:")  # FOR ENTER ELEMENT
    demo.append(element)
print(f"tuple is {tuple(demo)}")   # CONVER IN TUPLE AND PRINT
ele=input("enter element:")  # FOR ENTER ELEMENT
if ele in demo :                      # ELEMENT EXIST OR NOT
    print("element exists within a tuple")
else:
    print("element not exists within a tuple")    
