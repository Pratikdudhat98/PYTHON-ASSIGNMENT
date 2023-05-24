# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

a=int(input("ENTER NUMBER :")) # FOR INPUT
b=int(input("ENTER NUMBER :")) # FOR INPUT
c=int(input("ENTER NUMBER :")) # FOR INPUT
if a==b or b==c or a==c: # if two values are equal sum will be zero
    print("sum = 0")
else:
    print(f"sum is{a+b+c}" )    