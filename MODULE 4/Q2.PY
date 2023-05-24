# Write a Python program to read an entire text file.
f=open("pratik","w")   # OPEN FOR WRITING
f.write("you can do it\nalso do it\nbut very few moment you cannot do it")
f.close()
f=open("pratik","r")   # OPEN FOR READING
print(f.read())         # READING PRINT
f.close()
