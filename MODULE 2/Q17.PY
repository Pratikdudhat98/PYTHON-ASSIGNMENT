# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a=input("ENTER FIRST STRING:") # FOR INPUT
b=input("ENTER SECOUND STRING:") # FOR INPUT
c=b[:2]+a[2:]
d=a[:2]+b[2:]
print(c+" "+d)