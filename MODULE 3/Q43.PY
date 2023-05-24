# Write a Python program to print all unique values in a dictionary. 
dic1={1:"pow",2:"pok",3:"pow",4:"poj",5:"pok",6:"poi",7:"opi",8:"poi",9:"pow"}
dic1=dic1.values()  # SHOW ONLY VALUE
dic1=set(dic1)    # CONVERT IN SET
print(dic1)