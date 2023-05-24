# Write python program that swap two number with temp variable and without temp variable.

a=int(input("enter 1st number :")) # FOR INPUT
b=int(input("enter 2nd number :")) # FOR INPUT
print(f"BEFOR SWAP TWO NUMBER\n a={a}\n b={b}")  
print(f"AFTER SWAP TWO NUMBER\n a={b}\n b={a}")  # without using temp variable
temp=a                                        
a=b
b=temp
print(f"AFTER SWAP TWO NUMBER USING TEMP VARIABLE\n a={a}\n b={b}") # with using temp variable
