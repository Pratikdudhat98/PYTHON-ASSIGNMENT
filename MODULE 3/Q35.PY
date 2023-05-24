# Write a Python script to check if a given key already exists in a dictionary. 
dic1={1:456,3:567,4:789,5:984,6:154,9:698}
n=int(input("enter key :"))           # FOR INPUT OF KEY
dic1=dic1.keys()             # CONVERT IN LIST OF KEYS
if n in dic1 :                # CHECK KEY ALREADY EXIST OR NOT
    print("this key already exist in dictionary")       # PRINT IF ALREADY EXIST
else:
    print("this key not exist in dictionary")          # PRINT IF NOT EXIST