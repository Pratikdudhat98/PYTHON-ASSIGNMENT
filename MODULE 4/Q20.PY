# Write python program that user to enter only odd numbers, else will raise an exception.
n=int(input("enter number:"))
if n%2==0:
    raise Exception("please enter odd number")