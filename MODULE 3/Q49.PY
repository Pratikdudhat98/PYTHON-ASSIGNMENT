# Write a Python function to calculate the factorial of a number (a nonnegative integer) .
def fact(f):                          # FUNCTION CREATE 
    factorial=1                        
    for i in range(f,0,-1):          # RANGE USE
        factorial=factorial*i        # EACH ITERATOR MULTIPLY WITH FACTORIAL
    return factorial             
n=int(input("enter no for factorial:"))
print(f"factorial of {n} is {fact(n)}")       # PRINT FACTORIAL ANSWER