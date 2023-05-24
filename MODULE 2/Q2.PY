# Write a Python program to get the Factorial number of given number.

factorial=1
number=int(input("ENTER NUMBER FOR FACTORIAL :")) # FOR INPUT
for i in range(number,0,-1):
    factorial*=i
print(f"factorial of {number} is {factorial}")   # FOR PRINT  
    
