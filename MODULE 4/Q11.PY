# Write a Python program to write a list to a file.
a=["siuy","tyug","tuhjk","april"]
file=open("pralay.txt","w")    # FILE OPEN FOR WRITING
for i in a:
    file.write(i+"\n")  # WRITING LIST CONTENT+\n
file.close()
file=open("pralay.txt","r")
print(file.read())         # PRINT FILE READING