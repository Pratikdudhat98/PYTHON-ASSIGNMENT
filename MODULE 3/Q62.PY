# Write a Python program to calculate the area of a parallelogram.
def parallelogram(a,b): 
    return a*b                 # CALCULATE AREA
n1=int(input("enter base :"))           # INPUT BASE
n2=int(input("enter height :"))            # INPUT HEIGHT
print(f"AREA OF PARALLELOGRAM IS {parallelogram(n1,n2)}")