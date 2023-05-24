# Write a Python program to count the frequency of words in a file. 
from collections import Counter           # USE COLLECTION MODULE IN COUNTER FUNCTION
file=open("pratik.txt","r")        # OPEN FOR READ MODE
a=file.read().split()           # READ AND SPLIT WITH SPACE
print(collections.Counter(a))      
file.close()