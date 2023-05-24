# Write a Python program to get the Fibonacci series of given range.
n=int(input("given element for fibonacci series:")) # FOR INPUT
a=0
b=1
c=a+b
print(f"{a}\n{b}")   # PRINT 0 AND 1
i=3
while i<=n:      
    print(c)        
    a=b
    b=c
    c=a+b          
    i+=1             # FOR ITERATION UPDATE WITH 1
    

