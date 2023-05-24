# Write a python program to find the longest words.
n=input("enter sentences:")     # ENTER INPUT
n=n.split(" ")   # SPLIT THROUGH SPACE AND CONVERT IN LIST
a=""      # EMPTY STRING CREATE
for i in n:
    if len(i)>len(a):
        a=i
print(a)        # PRINT LONGEST WORDS 