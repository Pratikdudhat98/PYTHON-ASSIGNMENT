# Write a Python program to copy the contents of a file to another file. 
file=open("pratik.txt","r")   # SOURCE FILE OPEN FOR READ
file1=open("pralay.txt","w")  # DESTINATION FILE OPEN FOR WRITING PURPOSE
for x in file.read():    # IN FOR LOOP FILE READ
    file1.write(x)      # PRINT ALL READ CONTENT IN DESTINATION FILE
file.close()
file1.close()
file1=open("pralay.txt","r")
print(file1.read())    