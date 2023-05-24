# Write a Python function to reverses a string if its length is a multiple of 4.
a=input("ENTER STRING :") # FOR INPUT
print(f"length is {len(a)}")
if len(a)%4==0 :
    print(a[-1::-1]) # FOR reverse print