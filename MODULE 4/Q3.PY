# Write a Python program to append text to a file and display the text.
file=open("pratik.txt","a")           # OPEN FOR UPDATE
file.write("device\nyour way is your way")         # UPDATE DETAIL
file.close()
file=open("pratik.txt","r")  # OPEN FOR READ
print(file.read())  # PRINT READ
file.close()