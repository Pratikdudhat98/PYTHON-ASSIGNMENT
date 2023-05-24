# Write a Python function to check whether a number is perfect or not.
def perfect(n):
    sum=0              
    for i in range(1,n//2+1):      
        if n%i==0:               
            sum=sum+i
    if n==sum:                              # CHECK NO IS PERFECT OR NOT
        return "NUMBER IS PERFECT"
    else:
        return "NUMBER IS NOT PERFECT"    
a=int(input("enter number:"))                     # FOR INPUT
print(perfect(a))            
