a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :"))
print(f"BEFOR SWAP TWO NUMBER\n a={a}\n b={b}")  # without using temp variable
print(f"AFTER SWAP TWO NUMBER\n a={b}\n b={a}")  # with using temp variable
temp=a
a=b
b=temp
print(f"AFTER SWAP TWO NUMBER USING TEMP VARIABLE\n a={a}\n b={b}")
