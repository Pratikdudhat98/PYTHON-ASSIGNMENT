# Write a Python program to returns sum of all divisors of a number.
def calculation(a):
    sum =0
    for i in range (1,a):         
        if a%i==0:         # CHECK MODULOUS IS ZERO OR NOT
            sum+=i         # SUM OF DIVISIOR NO
    return sum
n=int(input("ENTER NUMBER :"))     # FOR INPUT
print(f"SUM OF DIVISOR IS {calculation(n)}")            