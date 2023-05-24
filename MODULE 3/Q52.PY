# Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(a):
    if a==a[-1::-1]:                 # CHECK STRING IS NOT PALINDROME OR NOT
        return "string is palindrome"
    else:
        return "string is not palindrome"
n=input("enter string:")                # FOR INPUT
print(palindrome(n))        