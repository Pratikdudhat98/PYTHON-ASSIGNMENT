""" Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string."""
a=input("ENTER STRING :") # FOR INPUT
b=a.find("not")  # FOR FIND INDEX
c=a.find("poor")  
if b < c :
    print(a.replace(a[b:c+4],"good")) # FOR REPLACE
