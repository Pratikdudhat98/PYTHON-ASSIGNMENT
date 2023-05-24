# Write a Python program to count the number of lines in a text file.
file=open("pratik.txt","r")
c=file.readlines()[:]           # READLINES THROUGH CONVERT ALL LINES IN LIST 
print(len(c))           # PRINT LIST LENGTH AND ALSO FIND LINES OF FILE