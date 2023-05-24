# Write a Python function to check whether a number is in a given range.
def calculation(a,b):
    if a in range(b):                               # CHECK GIVEN NO IN RANGE OR NOT
        return "this number in given range"
    else:
        return "this number not in given range"    
n=int(input("enter number for check :"))             # FOR INPUT CHECK NO
i=int(input("enter range:"))                  # FOR INPUT RANGE
print(calculation(n,i))
