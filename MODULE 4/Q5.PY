# Write a Python program to read last n lines of a file.
n=int(input("how many last lines read:"))
file=open("pratik.txt","r")     # OPEN FILE FOR READ
a=file.readlines()[-n:]         # FOR READ LAST N LINES
for i in a:
    print(i)          # PRINT READ LINE THROUGH FOR LOOP