"""Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} """
n=input("ENTER NAME:")     # ENTER STRING
dic1={}       # CREATE EMPTY DICTIONERY
for i in n:
    if i in dic1:       
        dic1[i]+=1   
    else:
        dic1[i]=1
print(dic1)            # PRINT DICTIONERY

