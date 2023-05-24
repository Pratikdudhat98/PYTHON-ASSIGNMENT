# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
list1=[]
n=int(input("last no of element in list :")) # FOR INPUT LAST ELEMENT
for i in range(1,n+1):
    list1.append(i**2)
print(list1[:5]+list1[-5:])    # PRINT SQUARE OF FIRST 5 AND LAST 5 OF LIST1
