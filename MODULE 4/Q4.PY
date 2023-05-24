# Write a Python program to read first n lines of a file.
n=int(input("how many lines print in file:"))         # FOR INPUT OF NO OF LINES
file=open("pratik.txt","r")      # FILE OPEN
for i in range(n):               # RUN FOR LOOP FOR NO OF LINE READ
    print(file.readline())       # PRINT READ LINE
file.close()